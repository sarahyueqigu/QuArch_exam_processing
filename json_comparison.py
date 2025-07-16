import boto3
from botocore.exceptions import ClientError
import config
import json
import os
import helper

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-2")

arn = config.claude_37

results = []

# If there are any discrepancies between the content (e.g. the material rather than the point values) 
# of each version of dictionaries/JSONs, the field "correctly_parsed" should be set to false, like 
# this:

prompt_false_checking = """You are are a JSON accuracy checker. Attatched are multiple versions of the same 
        content extracted in the format of a dictionary/json from different LLM models. Your task is to 
        compare the content of each dictionary/JSON field by field. Identify discrepancies in extracted 
        values, missing fields, or format differences. 

        Your output should be a dictionary like this, and ONLY this:
        {
            "question_id": <Insert the "question_id" from the txt file>, 
            "correctly_parsed": <true or false>
        }

        The LLM model claude_37 is typically best at extracting all the information. However, if the other
        subsequent models (e.g. claude_35, pixtral_large, llama_17b) contain content that is not included
        in the original claude_37 version of the extracted content, the field "correctly_parsed" should 
        be set to false, like this:
        {
            "question_id": "digitaltechnik-s21-en-sol/Problem_10/a", 
            "correctly_parsed": false
        }

        Be sure to include an explanation for why you would mark it as false. Otherwise,
        if the content between each LLM model has no discrepancies, your output should look
        like this:
        {
            "question_id": "digitaltechnik-s21-en-sol/Problem_10/a", 
            "correctly_parsed": true
        }
        
        Here is the format of exam content extraction input:
        LLM MODEL: <Insert LLM model name>
        EXTRACTED EXAM CONTENT:
        {
            “question_id”: “exam_name/Problem_number/subproblem_letter” (e.g. “a”, “b”, etc.),
            “context”: “<Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>“,
            “context_figures”: “file_directory_path/exam_name/img_number”,
            “question”: “<Insert the full question of the problem, exactly as it appears in the original>“,
            “solution”: “<Insert the full solution of the problem, exactly as shown in the original>“,
            “solution_figures”: “file_directory_path/exam_name/img_number”,
            “correctly_parsed”: “null” (indicating if the problem was parsed correctly).
        }
        Attatched below is each version of the actual extracted content from the exam
        """

# e.g. exam = "740_f13_midterm2_solutions"
def process_per_problem(exam):

# Attatched are (1) an exam pdf, (2) images extracted for that particular question, and (3)
    print("COMPARING JSON RESULTS")
    print("PROCESSING:", exam)

    input_dir = "out_model_comparison/" + exam

    # Open one JSON file to iterate thru the questions
    json_path = os.path.join(input_dir, "claude_37.json")
    with open(json_path, 'r', encoding='utf-8') as file:
        placeholder_problems = json.load(file)

    # Iterate through each question in each JSON
    for problem in placeholder_problems: 

        print("Processing", problem["question_id"])
        
        # If errors occur because the question_id doesn't work, use:
        # for index in enumerate(json_content):

        prompt = prompt_false_checking

        # Iterate through each output from each llm model
        for llm_model in os.listdir(input_dir):
            json_path = os.path.join(input_dir, llm_model)

            # Read JSON file as it is
            with open(json_path, 'r', encoding='utf-8') as file:
                problems_version = json.load(file)
            
            problem_content = next((item for item in problems_version 
                                    if item["question_id"] == problem["question_id"]), None)
            
            # Read the problem as a string to feed into the AI
            problem_str = json.dumps(problem_content, indent=2)  
            prompt += "\nLLM MODEL: " + llm_model + "\nEXTRACTED EXAM CONTENT: + \n" + problem_str 

        # Process the result
        result = claud_37_processing(prompt)
        print(result)

        json_str = helper.strip_json_code_block(result)
        json_result = json.loads(json_str)
        results.append(json_result)            

    os.makedirs("llm_verification_v2", exist_ok=True)
    output_path = os.path.join("llm_verification_v2", "[AUTOCHECK_V2]" +  exam + ".json")

    with open(output_path, 'w') as file:
        json.dump(results, file, indent=4)
    
    print("SAVED TO: ", output_path)


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
            inferenceConfig={"maxTokens": 8120, "temperature": 0.3},
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
    exam = "exam_solutions_ss2012"

    process_per_problem(exam)

    # for file in os.listdir(path):
    #     input_dir = os.path.join(path, file)
        