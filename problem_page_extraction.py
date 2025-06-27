import ast
import boto3
import fitz
import os
from botocore.exceptions import ClientError
import json
import nest_asyncio
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse


load_dotenv()
nest_asyncio.apply()

def extract_page_range(input_pdf_path, output_pdf_path, start_page, end_page):
    """
    Extract pages from start_page to end_page (1-based index, inclusive)
    and save as a new PDF.
    """
    doc = fitz.open(input_pdf_path)
    new_doc = fitz.open()

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

def claud_37_processing(path, filename):
    # get json version of PDF from Llamaparse
    parser = LlamaParse(
    api_key=os.getenv("LLAMAPARSE_API_KEY"),
    parse_mode="parse_page_with_llm",
    num_workers=4,       # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    )

    result = parser.parse(path)

    # create a temporary .txt file for storing the json (since claude doesn't take json input)
    
    txt_path = "page_numbers" + "/" + filename[:-4] + ".json"

    with open(txt_path, "w") as file:
        # Use json.dump() to write the data to the file
        json.dump(result.model_dump(), file, indent=4)


    # # Create a Bedrock Runtime client in the AWS Region you want to use.
    # client = boto3.client("bedrock-runtime", region_name="us-east-1")

    # # Set the model ID, e.g. Claude 3 Haiku.
    # model_id = "anthropic.claude-3-7-sonnet-20250219-v1:0"
   
    claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"

     # Load the txt document
    with open(txt_path, "rb") as file:
        document_bytes = file.read()

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


    # response_claude_thinking = invoke_model(claude_inference_profile_arn, conversation)
    # print("=== Claude 3.7 Sonnet With Thinking ===")
    # print(response_claude_thinking)



def execute(input_dir):
    # input_dir = "OnurETHZ_exams"

    os.makedirs("txt_files", exist_ok=True)

    for filename in os.listdir(input_dir):
        # Build full path
        input_path = os.path.join(input_dir, filename)

        
        # Only process PDFs
        if input_path.lower().endswith(".pdf"):
        # if input_path == "data/CDA 4205 Computer Architecture Exam 2 Practice Solution-3.pdf":
            print("Processing:", input_path)
            string_output = claud_37_processing(input_path, filename)
            print(string_output)

        
            # find the first “{” and the last “}”
            start = string_output.index("{")
            end   = string_output.rindex("}") + 1
            dict_text = string_output[start:end]

            # safely evaluate as a Python literal
            data = ast.literal_eval(dict_text)
            print(data)
            
            for problem in data:

                child_pdf_filename = problem + ".pdf"
                # output_dir = "extracted_problems/" + filename[:-4] + "/" + child_pdf_filename[:-4]
                output_dir = "extracted_problems/" + filename[:-4]

                # Create the target directory if it doesn't exist
                os.makedirs(output_dir, exist_ok=True)

                output_path = os.path.join(output_dir, child_pdf_filename)
                extract_page_range(input_path, output_path, data[problem][0], data[problem][1])