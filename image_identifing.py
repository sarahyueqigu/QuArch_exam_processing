import base64
import boto3
from botocore.exceptions import ClientError
import json
import os


client = boto3.client("bedrock-runtime", region_name="us-east-2")

prompt = """
You are a language model assisting with the digitization of academic exam content in Computer Architecture.
Input:
 You are provided with:
A PDF file containing one problem.


PNG images containing tables, diagrams, circuit schematics, or block diagrams that were part of this problem.


Each problem in the exam may contain:
A main context paragraph or a brief statement (e.g., “Convert the number 42 to binary”).
One or more sub-questions, or a single standalone question.
Sub-question-specific context that may be separate from both the main problem context and the sub-question text itself.
Multiple question parts embedded within a single sub-question.
Point values for problems or subproblems (including extra credit).
Solutions, which may be typed or handwritten.
Associated figures (tables, diagrams, circuits, or block diagrams).


Your task:
Match each visual element (table, diagram, circuit schematic, or block diagram) to its correct association in the exam. There are three main associations: the main problem, the sub-problem question, and the sub-problem solution. 

Specifically, determine whether each visual belongs to one of the following:
The main problem context (labelled as problem_figure)
A sub-problem context (subproblem_figure)  
A solution (solution_figure)

At times, the context or question in the main problem, sub-problem, sub-problem question, and/or sub-problem solution will include phrases (such as “The table below” or “The following diagram”) that indicate a visual image falls under that category. 

Your output should be a dictionary like this:

image_name.png: "problem_figure"
image_name(2).png: "subproblem_figure"
image_name(3).png: "subproblem_figure"
image_name(4).png: "subproblem_figure"

Each image_name should be replaced with the actual name of the image.

Be as precise as possible in your associations. 
"""


# Load the document
with open("separated_exam_pages/CDA 4205 Computer Architecture Exam 2 Practice Solution-3 1.pdf", "rb") as file:
    document_bytes = file.read()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

if __name__ == "__main__":
    claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"
    input_dir = "images/CDA 4205 Computer Architecture Exam 2 Practice Solution-3"
    

    for image_file in os.listdir(input_dir):
        # Build full path
        image_path = os.path.join(input_dir, image_file)
        image_base64 = encode_image(image_path)
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()


        # Start a conversation with a user message and the document
        conversation = [
            {
                "role": "user",
                "content": [
                    {"text": prompt},
                    {
                        "document": {
                            # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                            "format": "pdf",
                            "name": "Amazon Nova Service Cards",
                            "source": {"bytes": document_bytes},
                        }
                    },
                    {
                        "image": {
                            "format": "png",  
                            "source": {
                                "bytes": image_bytes  # must be raw image bytes, not base64
                            }
                        }
                    }
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
            print(response_text)

        except (ClientError, Exception) as e:
            print(f"ERROR: Can't invoke '{claude_inference_profile_arn}'. Reason: {e}")
            exit(1)