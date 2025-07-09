import base64
import boto3
from botocore.exceptions import ClientError
import json
import os

prompt = """
    You are a language model assisting with the digitization of academic exam content in Computer Architecture.

    Input:
    You are provided with:
    A PDF file containing one problem of an exam. If part of another problem is included, ignore this and only focus on {filename}.
    PNG images containing tables, diagrams, circuit schematics, or block diagrams that may or may not pertain to this problem.

    The given problem may be a standalone problem or consist of multiple sub-problems. Each problem or sub-problem may contain:
    Main context figures which are necessary to understanding the main problem, or ALL of the sub-problems.
    Sub-problem-specific figures that are separate from both the main problem context and the other sub-problems.
    Solutions to the main problem, which may be typed or handwritten.
    Solutions to a certain sub-problem, which may be typed or handwritten.


    Your task:
    Match each visual element (table, diagram, circuit schematic, or block diagram) to its correct association in the exam. 
    Each image should have one of the four possible associations: 
    The main problem question (labeled as problem_figure)
    The sub-problem question (labeled as subproblem_figure)
    The main problem solution (labeled as problem_solution)
    The sub-problem solution (labeled as subproblem_solution)

    At times, the context or question in the main problem/sub-problem question/solution will include phrases (such as “The table below” or “The following diagram”) that indicate a visual image falls under that category. 

    Your output should be a dictionary like this:

    [
        {{
            "name": "image_name.png",
            "type": "problem_figure",
            "part": ""
        }}
    ]


    If the figure is part of a subproblem, its output should represent the following, in which the "part" field is left unempty:
    [
        {{
            "name": "image_name.png",
            "type": "subproblem_figure",
            "part": "a" (or "A" or "1" or "i"; insert the part number/letter exactly as it appears)
        }}
    ]

    If a provided image is not part of {filename} and instead is part of other problem(s), omit it from the dictionary.
    Be as precise as possible in your associations. Only include the dictionary; don't include the reasoning.

    The names of the images provided are given below, in order:
    """

client = boto3.client("bedrock-runtime", region_name="us-east-2")

claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"

def process(exam_path, pages_data, output_fol): 
    print("\nIMAGE_IDENTIFYING")
    # Create a dictionary defining all problems' image matches
    matches = {}

    # page_ranges is the dictionary from problem_page_extraction that defined each problem's page range
    filename = os.path.basename(exam_path)
    problems_path = os.path.join(output_fol,filename[:-4]) #7/3 changed to generic output_fol instead of "extracted_problems"
    #problems_path = os.path.join("extracted_problems",filename[:-4])

    # Repeat for every problem that was extracted from exam
    for problem in os.listdir(problems_path):
        # Only process the problem PDFs, ignore the images folder
        if problem.lower().endswith(".pdf"):
            with open(os.path.join(problems_path, problem), "rb") as f:
                document_bytes = f.read()

            # Start a conversation with a user message and the document
            conversation = [
                {
                    "role": "user",
                    "content": [
                        {"text": prompt.format(filename = problem[:-4])},
                        {
                            "document": {
                                # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                                "format": "pdf",
                                "name": "Computer Architecture Exam Problem",
                                "source": {"bytes": document_bytes},
                            }
                        }
                    ],
                }
            ]

            # Add all relevant images to the AI "chat"
            problem_range = pages_data[problem[:-4]]

            # Only make this AI call if the problem has images to match
            if len(problem_range) > 2:
                for image_name in problem_range[2:]:
                    image_path = os.path.join("images", filename[:-4], image_name)
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

                    # Also append image name to prompt, for easier identification
                    conversation[0]["content"][0]["text"] += image_name + "\n"

                try:
                    # Send the message to the model, using a basic inference configuration.
                    response = client.converse(
                        modelId=claude_inference_profile_arn,
                        messages=conversation,
                        inferenceConfig={"maxTokens": 800, "temperature": 0.3},
                    )

                    # Extract and print the response text.
                    response_text = response["output"]["message"]["content"][0]["text"]
                    matches[problem] = json.loads(response_text)

                except (ClientError, Exception) as e:
                    print(f"ERROR: Can't invoke '{claude_inference_profile_arn}'. Reason: {e}")
                    exit(1)
                    
    return matches