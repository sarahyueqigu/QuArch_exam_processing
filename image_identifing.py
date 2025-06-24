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

[
  {
    "name": "image_name.png",
    "type": "problem_figure",
    "part": ""
  }
]


If the figure is part of a subproblem, its output should represent the following, in which the "part" field is left unempty:
[
  {
    "name": "image_name.png",
    "type": "subproblem_figure",
    "part": "a"
  }
]


Be as precise as possible in your associations. Only include the dictionary; don't include the reasoning.
"""

claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"

def encode_image(image_path):
    print(image_path)
    with open(image_path, "rb") as i:
        return base64.b64encode(i.read()).decode('utf-8')

     # Build full path
    image_path = os.path.join(input_dir, image_file)
    # image_base64 = encode_image(image_path)
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
                        "name": "Computer Architecture Exam",
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
        print(type(response_text))

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{claude_inference_profile_arn}'. Reason: {e}")
        exit(1)



def process(image_file, input_dir):
    print(input_dir)
    # Read bytes from the document
    with open(input_dir + ".pdf", "rb") as f:
        document_bytes = f.read()


    # Read the JSON file; don't process it if it's a bad JSON
    try:
        
        with open(input_dir + ".json", "r") as j:
            json_data = json.load(j)
    
    except json.JSONDecodeError as e:
        print("JSON decoding failed for", input_dir + ".json:")
        print(f"Error message: {e.msg}")
        print(f"Line: {e.lineno}, Column: {e.colno}, Char: {e.pos}")
        return
    
    for image in os.listdir(input_dir):
        image_path = os.path.join(input_dir, image)

        print("path 1: ", image_path)

        # image_base64 = encode_image(image_path)
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
                            "name": "Computer Architecture Exam",
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
        

        image_info = json.loads(response_text)

        # image_info["name"] = input_dir + "/" + image

        if image_info[0]["type"] == "problem_figure":
            json_data["problem_figures"].append(input_dir + "/" + image)
        else:
            # Find the specific part of probelm and extract its subproblem_figures
            # TODO: is there an easier/more efficient way to do this?
            for part in json_data.get("parts", []):
                if part.get("part") == image_info[0]["part"]:
                    for subproblem in part.get("subproblem", []):
                        subproblem_figures = subproblem.get("subproblem_figures", [])
                        subproblem_figures.append(input_dir + "/" + image)
        
        with open(input_dir + ".json", "w") as f:
            json.dump(json_data, f, indent=2)  # indent=2 makes it pretty-printed




if __name__ == "__main__":
    claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"
    input_dir = "extracted_problems/CDA 4205 Computer Architecture Exam 2 Practice Solution-3"


    for folder in os.listdir(input_dir):
        path = os.path.join(input_dir, folder)

        if os.path.isdir(path):

            print("path 1: ", path)

             # Read bytes from the document
            with open(path + ".pdf", "rb") as f:
                document_bytes = f.read()


            # Read the JSON file; don't process it if it's a bad JSON
            try:
                
                with open(path + ".json", "r") as j:
                    json_data = json.load(j)
            
            except json.JSONDecodeError as e:
                print("JSON decoding failed for", path + ".json:")
                print(f"Error message: {e.msg}")
                print(f"Line: {e.lineno}, Column: {e.colno}, Char: {e.pos}")
                continue

                        
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
                                "name": "Computer Architecture Exam",
                                "source": {"bytes": document_bytes},
                            }
                        }
                    ],
                }
            ]
            
            for image_file in os.listdir(path):
                print("image: ", image_file)

               
                # if image_file.lower().endswith(".png"):

                # Add all images to the AI "chat"

                # Build full path
                image_path = os.path.join(path, image_file)
                print("image_path", image_path)
                image_base64 = encode_image(image_path)
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
                    inferenceConfig={"maxTokens": 800, "temperature": 0.3},
                )

                # Extract and print the response text.
                response_text = response["output"]["message"]["content"][0]["text"]
                print(response_text)
                print(type(response_text))

            except (ClientError, Exception) as e:
                print(f"ERROR: Can't invoke '{claude_inference_profile_arn}'. Reason: {e}")
                exit(1)