import boto3
from botocore.exceptions import ClientError
import json
import os
from mistralai import Mistral

api_key = "IffIovWq8tUyBc2oinkenZXp2MeqnALs"
model = "mistral-small-latest"

client = boto3.client("bedrock-runtime", region_name="us-east-2")

#PROMPT
prompt = """You are a language model assisting with the digitization of academic exam content. The input is an exam which has been parsed into Markdown text. The exam contains one or more problems from a Computer Architecture assessment. A problem may include any combination of the following:
A context paragraph, or just a short statement (e.g., “Convert the number 42 to binary”)
One or more sub-questions, or be a single standalone question
Context for sub-questions separate from the sub-question and separate from the original problem context
Multiple questions within a subquestion
Point value associations for the problem or subproblems, including extra credit points
Solutions, either typed or handwritten
Tables, diagrams, circuit schematics, or block diagrams
Your task is to identify and separate each exam problem into the listed components, including context, sub-questions, figures, and solutions. At times, a subquestion can have nested subparts. Ignore any point values for any problem, question, or sub-question. Format your response using the template below. If the particular exam question lacks any of the listed components, do not include them.

Please format the data so that it can be exported into a JSON file. It should follow the following template.

{
  "exam_name": <Copy the exact name of the file>,
  "problems": [
    {
      "problem": <Copy the problem number and/or information>,
      "problem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>,
      "problem_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence]
      "parts": [
        {
          "part": <Insert part number or letter, e.g., 1 or a. If no subproblem parts exist, just use the below question and solutions structure>,
          "subproblem": [
            {
              "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header>,
              "subproblem_question": <Insert the full text of the question, exactly as it appears in the original>,
              "subproblem_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence]
              }
          ]
          "answer": [
            {
              "solution": <Insert the full solution exactly as shown in the original>,
              "solution_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence]
            }
          ]
        }
        {
          "part": <Insert part number or letter, e.g., 1 or a. If no subproblem parts exist, just use the below question and solutions structure>,
          "subproblem": [
            {
              "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header>,
              "subproblem_question": <Insert the full text of the question, exactly as it appears in the original>,
              "subproblem_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence]
              }
          ]
          "answer": [
            {
              "solution": <Insert the full solution exactly as shown in the original>,
              "solution_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence]
            }
          ]
            // ...repeat as needed for additional Q&A pairs within this part
        }
      ]
      "problem": <Copy the problem number and/or information>,
      "problem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>,
      "problem_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence]
      "parts": [
        {
          "part": <Insert part number or letter, e.g., 1 or a. If no subproblem parts exist, just use the below question and solutions structure>,
          "subproblem": [
            {
              "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header>,
              "subproblem_question": <Insert the full text of the question, exactly as it appears in the original>,
              "subproblem_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence]
              }
          ]
          "answer": [
            {
              "solution": <Insert the full solution exactly as shown in the original>,
              "solution_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence]
            },
          ]
            // ...repeat as needed for additional Q&A pairs within this part
        }
      ]
    }
  ]
}

"""

def invoke_model(inference_profile_arn, payload):
    """
    Sends an InvokeModel request using the inference profile ARN.
    Returns the decoded JSON response.
    """
    request_body = json.dumps(payload)
    try:
        response = client.invoke_model(modelId=inference_profile_arn, body=request_body)
    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke model '{inference_profile_arn}': {e}")
        return None
    return json.loads(response["body"].read())


def mistral_processing(path):

    # If local document, upload and retrieve the signed url
    uploaded_pdf = client.files.upload(
      file={
        "file_name": path,
        "content": open(path, "rb"),
      },
      purpose="ocr"
    )
    signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)

    # Define the messages for the chat
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "document_url",
                    "document_url": signed_url.url
                }
            ]
        }
    ]
    # Get the chat response
    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )
    return chat_response.choices[0].message.content


def claud_37_processing(path):
    # # Create a Bedrock Runtime client in the AWS Region you want to use.
    # client = boto3.client("bedrock-runtime", region_name="us-east-1")

    # # Set the model ID, e.g. Claude 3 Haiku.
    # model_id = "anthropic.claude-3-7-sonnet-20250219-v1:0"

   
    claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"

    # # --- A. With Thinking Enabled ---
    # claude_thinking_payload = {
    #     "anthropic_version": "bedrock-2023-05-31",
    #     "max_tokens": 24000,
    #     "thinking": {
    #         "type": "enabled",
    #         "budget_tokens": 1500
    #     },
    #     "messages": [
    #         {
    #             "role": "user",
    #             "content": prompt
    #         }
    #     ]
    # }


     # Load the document
    with open(path, "rb") as file:
        document_bytes = file.read()

    # Start a conversation with a user message and the document
    conversation = [
        {
            "role": "user",
            "content": [
                {"text": "Briefly compare the models described in this document"},
                {
                    "document": {
                        # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                        "format": "pdf",
                        "name": "Amazon Nova Service Cards",
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
            inferenceConfig={"maxTokens": 500, "temperature": 0.3},
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        print(response_text)

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{claude_inference_profile_arn}'. Reason: {e}")
        exit(1)


    response_claude_thinking = invoke_model(claude_inference_profile_arn, claude_thinking_payload)
    print("=== Claude 3.7 Sonnet With Thinking ===")
    print(response_claude_thinking)



if __name__ == "__main__":
    input_dir = "data"

    for filename in os.listdir(input_dir):
        # Build full path
        input_path = os.path.join(input_dir, filename)
        
        
        # Only process PDFs
        if input_path.lower().endswith(".pdf"):
            print("Processing:", input_path)
            # Now `filepath` is the path to one PDF file
             # Open both libraries’ handles
            path = "data/" + filename

            json_filename = filename[:-4] + "_problems.json"

            output_dir = "json_v2" 

            # Create the target directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, json_filename)

            # json_text = mistral_processing(filename)
            json_text = claud_37_processing(path)
            print(json_text)

            
            # Write the same data out to destination file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(json_text)
