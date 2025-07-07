import ast
import boto3
import pymupdf
import os
import asyncio
from botocore.exceptions import ClientError
import json
import nest_asyncio
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse

load_dotenv()
nest_asyncio.apply()

parser = LlamaParse(
    api_key="llx-K1mUygWh37kvgzJbCvvdROrM8N5XBfQFdM3mXfgye1GzYJtZ",
    parse_mode="parse_page_with_llm",
    extract_charts=True,
    num_workers=4,       # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    )



def extract_page_range(input_pdf_path, output_pdf_path, start_page, end_page):
    """
    Extract pages from start_page to end_page (1-based index, inclusive)
    and save as a new PDF.
    """
    doc = pymupdf.open(input_pdf_path)
    new_doc = pymupdf.open()

    # PyMuPDF uses 0-based indexing
    new_doc.insert_pdf(doc, from_page=start_page - 1, to_page=end_page - 1)

    new_doc.save(output_pdf_path)
    new_doc.close()
    doc.close()
    print(f"Extracted pages {start_page} to {end_page} into '{output_pdf_path}'")



client = boto3.client("bedrock-runtime", region_name="us-east-2")

#PROMPT
prompt = """
You are given a multi-page PDF exam answer key. Your task is to split this document into sections based on each main problem (e.g., Problem 1, Problem 2, etc.).

Subproblems (like 1a, 1b, 1.1, 1.2, etc.) should not be separated out — they must stay within the same range of pages as their main problem. For each problem, provide:

The problem number

The start and end page numbers (inclusive) that cover that problem and all its subproblems

Use the headings or clear textual cues such as “Problem X”, “Question X”, or similar phrases to detect problem boundaries. If a problem spans multiple pages, include all relevant pages in its range.

Output your result as dictionary like this:
{
    "Problem_1": [1, 2],
    "Problem_2": [2, 5],
    "Problem_3": [6, 7]
}
"""
async def llama_processing(file_path, output_dir):
    # get json version of PDF from Llamaparse 
    # store the json for document input into the claude prompt   
    result = await parser.aparse(file_path)

    # Create the image directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    #Save all images in the exam to a designated folder
    await result.asave_all_images(output_dir)

    # then save each chart image by name
    for page in result.pages:
        for chart in page.charts:
            await result.asave_image(chart.name, output_dir)
    
    print("Saved exam images to ", output_dir)

    #Also return the document json
    return result


def claud_37_processing(document_bytes):
    claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"

    # Start a conversation with a user message and the document
    conversation = [
        {
            "role": "user",
            "content": [
                {"text": prompt},
                {
                    "document": {
                        # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                        "format": "txt",
                        "name": "Computer Architecture Exam",
                        "source": {"bytes": document_bytes},
                    }
                },
            ],
        }
    ]

    try:
        # Send the message to the model, using a basic inference configuration.
        response = client.converse(
            modelId=claude_inference_profile_arn,
            messages=conversation,
            inferenceConfig={"maxTokens": 800, "temperature": 0.3},
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{claude_inference_profile_arn}'. Reason: {e}")
        exit(1)


def process(input_path, output_fol): #7/3 added extra input path parameter, output_fol, such that all the output is not hard coded to "extracted_problems"
    print("\nPROBLEM_PAGE_EXTRACTION: ", input_path)
    
    filename = os.path.basename(input_path)

    # Save all images first
    images_path = os.path.join("images", filename[:-4])
    document_json = asyncio.run(llama_processing(input_path, images_path))
    # Convert the json to byte form for Claude input
    document_bytes = json.dumps(document_json.model_dump(), indent=4).encode("utf-8")

    #get the dictionary of split page numbers
    string_output = claud_37_processing(document_bytes)

    # find the first “{” and the last “}”
    start = string_output.index("{")
    end   = string_output.rindex("}") + 1
    dict_text = string_output[start:end]

    # convert to a real Python dictionary
    data = ast.literal_eval(dict_text)
    print(data)
    
    for problem in data:
        child_pdf_filename = problem + ".pdf"

        output_path = os.path.join(output_fol, filename[:-4], child_pdf_filename) #7/3 changed the "extracted_problems" to generic output_fol
        #output_path = os.path.join("extracted_problems", filename[:-4], child_pdf_filename) 
        
        # Create the target directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        extract_page_range(input_path, output_path, data[problem][0], data[problem][1])
        # Also sort all images from the relevant page ranges into the data dict
        for pagenum in range(data[problem][0]-1, data[problem][1]):
            for image in document_json.pages[pagenum].images:
                data[problem].append(image.name)
            for chart in document_json.pages[pagenum].charts:
                data[problem].append(chart.name)

    return data
