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
    
    input_dir = "out_model_comparison/" + exam

    # Open one JSON file to iterate thru the questions
    json_path = os.path.join(input_dir, "claude_37.json")
    with open(json_path, 'r', encoding='utf-8') as file:
        placeholder_problems = json.load(file)

    # Iterate through each question in each JSON
    for problem in placeholder_problems: 
        
        # If errors occur because the question_id doesn't work, use:
        # for index in enumerate(json_content):

        # Iterate through each output from each llm model
        for llm_model in os.listdir(input_dir):
            json_path = os.path.join(input_dir, llm_model)

            # Read JSON file as it is
            with open(json_path, 'r', encoding='utf-8') as file:
                problems_version = json.load(file)
            
            problem_content = next((item for item in problems_version 
                                    if problems_version["question_id"] == problem["question_id"]), None)
            

            print("problem_content:", problem_content)




            json_path = os.path.join(input_dir, llm_model)

            # Read JSON file as it is
            with open(json_path, 'r', encoding='utf-8') as file:
                json_problems = json.load(file)
            
            # Read the problem as a string to feed into the AI
            problem_str = json.dumps(json_problems, indent=2)

            prompt += """LLM model: """ + llm_model + "\n Extracted exam content:\n" + problem_str 
    
    
    result = claud_37_processing(prompt)
    print("\n \nRESULT:\n")

    json_str = helper.strip_json_code_block(result)
    print(json_str)
    json_result = json.loads(json_str)

    os.makedirs("llm_verification_v2", exist_ok=True)
    output_path = os.path.join("llm_verification_v2", exam + ".json")

    with open(output_path, 'w') as file:
        json.dump(json_result, file, indent=4)
    
    print("SAVED TO: ", output_path)

    # print(prompt)

   

    


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
            inferenceConfig={"maxTokens": 8120, "temperature": 0.1},
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
    exam = "740_f13_midterm2_solutions"

    process(exam)

    # for file in os.listdir(path):
    #     input_dir = os.path.join(path, file)
        