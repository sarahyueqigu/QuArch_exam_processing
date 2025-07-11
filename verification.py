import boto3
from botocore.exceptions import ClientError
import json
import os
import helper


# Send and process a document with Llama on Amazon Bedrock.

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-2")

# Set the model ID, e.g. Llama 3.1 8B Instruct.

# TODO: turn this into a dictionary and loop through them later

claude_37_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"

claude_35_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-5-sonnet-20241022-v2:0"

llama_17b_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.meta.llama4-scout-17b-instruct-v1:0"

pixtral_large_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.mistral.pixtral-large-2502-v1:0"

arns = {
    "claude_37_arn": "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    "claude_35_arn": "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    # "llama_17b_arn": "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.meta.llama4-scout-17b-instruct-v1:0",
    "pixtral_large_arn": "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.mistral.pixtral-large-2502-v1:0"


}

def process(json_path, exam):


    orign_prompt = """Attatched are (1) an exam pdf, (2) some of the contents from that exam extracted in json 
    format (either an entire problem or a subproblem), and (3) images extracted for that particular 
    question. Your task is to determine if the extracted content (text and images) are extracted 
    faithfully from the exam pdf.

    Your output should be a dictionary like this, and ONLY this:
    {
        "question_id": <Insert the "question_id" from the txt file>, 
        "correctly_parsed": <true or false>
    }

    For example, the output to a correctly parsed question for "digitaltechnik-s21-en-sol/Problem_10/a" would look like this:
    {
        "question_id": "digitaltechnik-s21-en-sol/Problem_10/a", 
        "correctly_parsed": true
    }

    If the question was parsed incorrect (e.g. if the images are extracted/cropped incorrectly, or if 
    the solution does not reflect the content in the exams, or if an image is categorized context_figures
    when it should be categorized in solution_figures) the output should look like this

    For example, the output to a correctly parsed question for "digitaltechnik-s21-en-sol/Problem_10/a" 
    would look like this:
    {
        "question_id": "digitaltechnik-s21-en-sol/Problem_10/a", 
        "correctly_parsed": false
    }

    """

    output = []

    # Read JSON file as it is
    with open(json_path, 'r', encoding='utf-8') as file:
        json_problems = json.load(file)
    
    # Create the folder where json results chekced by different APIs will be stored
    output_dir = "verification_tests/" + exam
    os.makedirs(output_dir, exist_ok=True)

    for arn in arns:
        print("ARN:", arn)

        for problem in json_problems:
            question_id = problem.get("question_id") # E.g. "digitaltechnik-s21-en-sol/Problem_10/a"

            # Get the exam name and the problem number as a path dir
            path_info = question_id.strip(os.sep).split(os.sep)
            problem_dir = path_info[0] + "/" + path_info[1] # E.g. "digitaltechnik-s21-en-sol/Problem_10"

            pdf_path = "extracted_problems/" + problem_dir + ".pdf"

            # Read the problem as a string to feed into the AI
            problem_str = json.dumps(problem, indent=2)

            print("PROCESSING PROBLEM: " + question_id)

            prompt = orign_prompt + """\nHere is the format of exam content extraction

            “question_id”: “exam_name/Problem_number/subproblem_letter” (e.g. “a”, “b”, etc.),
            “context”: “<Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>“,
            “context_figures”: “file_directory_path/exam_name/img_number”,
            “question”: “<Insert the full question of the problem, exactly as it appears in the original>“,
            “solution”: “<Insert the full solution of the problem, exactly as shown in the original>“,
            “solution_figures”: “file_directory_path/exam_name/img_number”,
            “correctly_parsed”: “null” (indicating if the problem was parsed correctly).
            
            Attatched below is the actual extracted content from the exam\n""" + problem_str

            # Load the document
            with open(pdf_path, "rb") as file:
                document = file.read()

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
                                "source": {"bytes": document},
                            }
                        },
                    ],
                }
            ]

            for image_path in problem.get("context_figures"):
                with open(image_path, "rb") as image_file:
                    image_bytes = image_file.read()

                # Append image to conversation
                conversation[0]["content"].append(
                    {
                        "image": {
                            "format": "png",
                            # "name": "context_figures: " + image_path,
                            "source": {
                                "bytes": image_bytes 
                            }
                        }
                    }
                )

            for image_path in problem.get("solution_figures"):
                with open(image_path, "rb") as image_file:
                    image_bytes = image_file.read()
                
                # Append image to conversation
                conversation[0]["content"].append(
                    {
                        "image": {
                            "format": "png",
                            # "name": "solution_figures: " + image_path,
                            "source": {
                                "bytes": image_bytes 
                            }
                        }
                    }
                )

            try:
                # Send the message to the model, using a basic inference configuration.
                response = client.converse(
                    modelId=arns[arn],
                    messages=conversation,
                    inferenceConfig={"maxTokens": 500, "temperature": 0.3},
                )

                # Extract and print the response text.
                response_text = response["output"]["message"]["content"][0]["text"]

                result = json.loads(helper.strip_json_code_block(response_text))
                output.append(result)                
                
            except (ClientError, Exception) as e:
                print(f"ERROR: Can't invoke '{arns[arn]}'. Reason: {e}")
                exit(1)

            output_path = os.path.join(output_dir, arn + ".json")

            with open(output_path, 'w') as file:
                json.dump(output, file, indent=4) 
    
    
   
if __name__ == "__main__":
    exam = "740_f13_midterm2_solutions.json"
    parent_dir = os.path.join("output", exam)
    process(parent_dir, exam[:-5])

    # for file in os.listdir(path):
    #     input_dir = os.path.join(path, file)
        