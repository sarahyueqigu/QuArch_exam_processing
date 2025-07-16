import base64
import boto3
from botocore.exceptions import ClientError
import json
import os
from botocore.config import Config

prompt = """
    You are a language model assisting with the digitization of academic exam content in Computer Architecture.

    Input:
    You are provided with:
    1) A PDF file containing one problem of an exam. If part of another problem is included, ignore this and only focus on {filename}.
    2) A .json-styled txt file containing the problem's extracted text. It may contain some or all of the following empty-list fields: "problem_context_figures", "subproblem_context_figures", "subproblem_solution_figures", and "problem_solution_figures".
    3) PNG images containing tables, diagrams, circuit schematics, or block diagrams that may or may not pertain to this problem. The names of the images provided are as follows, in order: {images}


    The given problem may be a standalone problem or consist of multiple sub-problems. Each problem or sub-problem may contain:
    Main context figures which are necessary to understanding the main problem, or ALL of the sub-problems.
    Sub-problem-specific figures that are separate from both the main problem context and the other sub-problems.
    Solutions to the main problem, which may be typed or handwritten.
    Solutions to a certain sub-problem, which may be typed or handwritten.


    Your task:
    Match each visual element (table, diagram, circuit schematic, or block diagram) to its correct association in the exam. 
    Each image should have one of the four possible associations: 
    The main problem question (belongs to "problem_context_figures")
    The sub-problem question (belongs to "subproblem_context_figures")
    The main problem solution (belongs to "problem_solution_figures")
    The sub-problem solution (belongs to "subproblem_solution_figures")

    At times, the context or question in the main problem/sub-problem question/solution will include phrases (such as “The table below” or “The following diagram”) that indicate a visual image falls under that category. 

    Your output should be a modified version of the given json, but with each of the "problem_context_figures"/"subproblem_context_figures"/"problem_solution_figures"/"subproblem_solution_figures" fields populated with lists of the relevant image paths, like the example below:
    "problem_context_figures": ["image_name.png", "image_name_2.png"]

    If a provided image is not part of {filename} and instead is part of other problem(s), omit it from the dictionary.
    Be as precise as possible in your associations. Only include the dictionary; don't include the reasoning. 
    If none of the images given pertain to the problem, just output the original json given.
    """

config = Config(read_timeout=1000)
client = boto3.client("bedrock-runtime", region_name="us-east-2", config=config)

claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"

def process(exam_name, problem_pdf, problem_json, images): 
    filename = os.path.basename(problem_pdf)
    print("Matching images in: ", filename)

    # get the problem pdf
    with open(problem_pdf, "rb") as f:
        document_bytes = f.read()
    # get the problem's text-extracted json and convert to byte form 
    json_bytes = json.dumps(problem_json, indent=4).encode("utf-8")


    # Start a conversation with a user message and the document
    conversation = [
        {
            "role": "user",
            "content": [
                {"text": prompt.format(filename = filename[:-4], images=images)},
                {
                    "document": {
                        # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                        "format": "pdf",
                        "name": "Computer Architecture Exam Problem PDF",
                        "source": {"bytes": document_bytes},
                    }
                },
                {
                    "document": {
                        # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                        "format": "txt",
                        "name": "Problem json File",
                        "source": {"bytes": json_bytes},
                    }
                }
            ],
        }
    ]


    # Add image files to conversation
    for image in images:
        image_path = os.path.join("images", exam_name, image)
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        # Append image to conversation
        conversation[0]["content"].append(
            {
                "image": {
                    "format": "png",
                    "source": {
                        "bytes": image_bytes 
                    }
                }
            }
        )

    try:
        # Send the message to the model, using a basic inference configuration.
        response = client.converse(
            modelId=claude_inference_profile_arn,
            messages=conversation,
            inferenceConfig={"maxTokens": 8120, "temperature": 0},
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        # print("images filled in: ", response_text)

        return json.loads(response_text)

    except ClientError as e:
        print(f"CLIENT ERROR: Can't invoke '{claude_inference_profile_arn}'. Reason: {e}")
        exit(1)
    except Exception as e:
        print("Prompt: ", conversation[0]["content"])
        print("Response text: ", response_text)
        print(f"EXCEPTION: {e}")
        exit(1)

