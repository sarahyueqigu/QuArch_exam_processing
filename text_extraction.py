import json
import os
from mistralai import Mistral

api_key = "IffIovWq8tUyBc2oinkenZXp2MeqnALs"
model = "mistral-small-latest"

client = Mistral(api_key=api_key)

#PROMPT
prompt = """You are a language model assisting with the digitization of academic exam content. The input is an exam which has been parsed into Markdown text. The exam contains one or more problems from a Computer Architecture assessment. A problem may include any combination of the following:
A context paragraph, or just a short statement (e.g., “Convert the number 42 to binary”)
One or more sub-questions, or be a single standalone question
Context for sub-questions separate from the sub-question and separate from the original problem context
Multiple questions within a subquestion
Point value associations for the problem or subproblems, including extra credit points
Solutions, either typed or handwritten
Tables, diagrams, circuit schematics, or block diagrams
Your task is to identify and separate each exam problem into the listed components, including context, sub-questions, figures, and solutions. Ignore any point values for any problem, question, or sub-question. Format your response using the template below. If the particular exam question lacks any of the listed components, do not include them.

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
          "question": [
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
          "question": [
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
          "question": [
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
          "question": [
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

def mistral_processing(filename):
    # Open both libraries’ handles
    path = "data/" + filename

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


if __name__ == "__main__":
    input_dir = "data"

    for filename in os.listdir(input_dir):
        # Build full path
        input_path = os.path.join(input_dir, filename)
        
        
        # Only process PDFs
        if input_path.lower().endswith(".pdf"):
            print("Processing:", input_path)
            # Now `filepath` is the path to one PDF file

            json_filename = filename[:-4] + "_problems.json"

            output_dir = "json" 

            # Create the target directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, json_filename)

            json_text = mistral_processing(filename)
            print(json_text)

            
            # Write the same data out to destination file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(json_text)
