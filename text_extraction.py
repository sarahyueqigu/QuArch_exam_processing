import boto3
from botocore.exceptions import ClientError
import os
import sys

# from mistralai import Mistral


client = boto3.client("bedrock-runtime", region_name="us-east-2")


# api_key = "IffIovWq8tUyBc2oinkenZXp2MeqnALs"
# model = "mistral-small-latest"

# def mistral_processing(path):

#     # If local document, upload and retrieve the signed url
#     uploaded_pdf = client.files.upload(
#       file={
#         "file_name": path,
#         "content": open(path, "rb"),
#       },
#       purpose="ocr"
#     )
#     signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)

#     # Define the messages for the chat
#     messages = [
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": prompt
#                 },
#                 {
#                     "type": "document_url",
#                     "document_url": signed_url.url
#                 }
#             ]
#         }
#     ]
#     # Get the chat response
#     chat_response = client.chat.complete(
#         model=model,
#         messages=messages
#     )
#     return chat_response.choices[0].message.content


def claud_37_processing(path, filename):
    claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"

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
      "problem": <Copy the problem number and/or information>,
      "problem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>,
      "problem_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence. If there are none, include this field as an empty array.]
      "parts": [
        {
          "part": <Insert part number or letter, e.g., 1 or a. If no subproblem parts exist, just use the below question and solutions structure>,
          "subproblem": [
            {
              "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header>,
              "subproblem_question": <Insert the full text of the question, exactly as it appears in the original>,
              "subproblem_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence.  If there are none, include this field as an empty array.]
              }
          ]
          "answer": [
            {
              "solution": <Insert the full solution exactly as shown in the original>,
              "solution_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence.  If there are none, include this field as an empty array.]
            }
          ]
        }
        {
          "part": <Insert part number or letter, e.g., 1 or a. If no subproblem parts exist, just use the below question and solutions structure>,
          "subproblem": [
            {
              "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header>,
              "subproblem_question": <Insert the full text of the question, exactly as it appears in the original>,
              "subproblem_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence.  If there are none, include this field as an empty array.]
              }
          ]
          "answer": [
            {
              "solution": <Insert the full solution exactly as shown in the original>,
              "solution_figures": [Indicate if there is a table(s) and/or image(s) here pertaining to the general problem context only by stating "IMAGE" or "TABLE" for each occurence.  If there are none, include this field as an empty array.]
            }
          ]
            // ...repeat as needed for additional Q&A pairs within this part
        }
      ]
    }

    """

    prompt += "\nThere may be multiple problems in the pdf, or only one. If there are multiple, do this for " + filename + "only."
     # Load the document
    with open(path, "rb") as file:
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
                        "format": "pdf",
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
            inferenceConfig={"maxTokens": 6000, "temperature": 0.2},
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        # print(response_text)
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{claude_inference_profile_arn}'. Reason: {e}")
        exit(1)



def process(filename, input_dir, output_dir):
    print("Processing text in:", filename)
    json_filename = filename[:-4] + ".json"

    output_path = os.path.join(output_dir, json_filename)

    # json_text = mistral_processing(filename)
    json_text = claud_37_processing(input_dir, filename[:-4])
    stripped_json = strip_json_code_block(json_text)

    # Write the same data out to destination file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(stripped_json)
    

    # # Kind of unncessary but if we want to label the JSONs

    # with open(output_path, 'r') as f:     
    #     data = json.load(f) 

    # # Change the exam name
    # data["exam_name"] = filename

    # json.dump(data, f, indent=2)
  


def strip_json_code_block(text: str) -> str:
    # Remove opening and closing code block markers
    lines = text.strip().splitlines()
    cleaned_lines = [line for line in lines if not line.strip().startswith("```")]
    return "\n".join(cleaned_lines)



# if __name__ == "__main__":
#     parent_folder = "extracted_problems"
#     print(os.listdir(parent_folder))
#     os.makedirs("extracted_problems", exist_ok=True)

#     for folder in os.listdir(parent_folder):
#         # Build full path
#         for filename in os.listdir(folder):
          

#           # Only process PDFs
#           if filename.lower().endswith(".pdf"):
#           # if input_path == input_dir + "/CDA 4205 Computer Architecture Exam 2 Practice Solution-2":
#               print("Processing:", filename)

#               path = folder + "/" + parent_folder + "/" + filename
#               json_filename = filename[:-4] + ".json"

#               output_dir = "json" 

#               # Create the target directory if it doesn't exist
#               os.makedirs(output_dir, exist_ok=True)
#               output_path = os.path.join(output_dir, json_filename)

#               # json_text = mistral_processing(filename)
#               json_text = claud_37_processing(path)
#               print(json_text)

              
#               # Write the same data out to destination file
#               with open(output_path, 'w', encoding='utf-8') as f:
#                   f.write(json_text)
