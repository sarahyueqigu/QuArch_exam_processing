import boto3
from botocore.exceptions import ClientError
import config
import json
import os
import helper

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-2")

arn = config.claude_37

# e.g. 
def process(exam):

# Attatched are (1) an exam pdf, (2) images extracted for that particular question, and (3)

    prompt = """You are are a JSON accuracy checker. Attatched are multiple versions of the same 
    content extracted in the format of a dictionary/json from different LLM models. Your task is to 
    compare the content of each dictionary/JSON field by field. Identify discrepancies in extracted 
    values, missing fields, or format differences. 

    Your output should be a dictionary like this, and ONLY this:
    [
        {
            "question_id": <Insert the "question_id" from the txt file>, 
            "correctly_parsed": <true or false>
        },
        {
            "question_id": <Insert the "question_id" from the txt file>, 
            "correctly_parsed": <true or false>
        },
        {
            "question_id": <Insert the "question_id" from the txt file>, 
            "correctly_parsed": <true or false>
        },
        {
            ... repeat for as many problems there are in each content extraction JSON
        },
    ]

    If there are any discrepancies between the content (e.g. the material rather than the point values) 
    of each version of dictionaries/JSONs, the field "correctly_parsed" should be set to false, like 
    this:
    {
        "question_id": "digitaltechnik-s21-en-sol/Problem_10/a", 
        "correctly_parsed": false
    }
     
     Here is the format of exam content extraction:
        “question_id”: “exam_name/Problem_number/subproblem_letter” (e.g. “a”, “b”, etc.),
        “context”: “<Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>“,
        “context_figures”: “file_directory_path/exam_name/img_number”,
        “question”: “<Insert the full question of the problem, exactly as it appears in the original>“,
        “solution”: “<Insert the full solution of the problem, exactly as shown in the original>“,
        “solution_figures”: “file_directory_path/exam_name/img_number”,
        “correctly_parsed”: “null” (indicating if the problem was parsed correctly).
        
    Attatched below is each version of the actual extracted content from the exam

    """
    
    input_dir = "out_model_comparison/" + exam[:-5]
    # Iterate through each output from each llm model
    for llm_model in os.listdir(input_dir):
        json_path = os.path.join(input_dir, llm_model)

        # Read JSON file as it is
        with open(json_path, 'r', encoding='utf-8') as file:
            json_problems = json.load(file)
        
        # Read the problem as a string to feed into the AI
        problem_str = json.dumps(json_problems, indent=2)

        prompt += """LLM model: """ + llm_model + "\n Extracted exam content:\n" + problem_str 
    
    result = claud_37_processing(prompt)

    json_result = helper.strip_json_code_block(result)

    # with open(preprocessed_output + "/" + problem + ".json", 'w') as file:
    #     json.dump(problem_dict, file, indent=4)

    print(prompt)

    print("\n \nRESULT:\n")
    print(result)

    


def claud_37_processing(prompt):

    # Start a conversation with a user message and the document
    conversation = [
        {
            "role": "user",
            "content": [
                {"text": prompt},
            ],
        }
    ]

    try:
        # Send the message to the model, using a basic inference configuration.
        response = client.converse(
            modelId=arn,
            messages=conversation,
            inferenceConfig={"maxTokens": 8000, "temperature": 0},
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{arn}'. Reason: {e}")
        exit(1)

# Send and process a document with Llama on Amazon Bedrock.

# Set the model ID, e.g. Llama 3.1 8B Instruct.

# TODO: turn this into a dictionary and loop through them later
   
if __name__ == "__main__":
    exam = "740_f13_midterm2_solutions.json"

    process(exam)

    # for file in os.listdir(path):
    #     input_dir = os.path.join(path, file)
        