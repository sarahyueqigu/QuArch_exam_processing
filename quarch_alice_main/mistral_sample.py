from mistralai import Mistral
import os
import argparse
import json

api_key = "6kH3nw0ytZnYPrjHF7Pk2WPpLeCjIqMx"
os.environ["mistral_api_key"] = api_key

client = Mistral(api_key=api_key)

#_______________________________________
# Mistral AI Prompt
#_______________________________________
prompt = """
You are a language model assisting with the digitization of academic exam content. The input is a .pdf file of an exam. The exam contains one or more problems from a Computer Architecture assessment. A problem may include any combination of the following:
A context paragraph, or just a short statement (e.g., “Convert the number 42 to binary”)
One or more sub-questions, or be a single standalone question
Context for sub-questions separate from the sub-question and separate from the original problem context
Multiple questions within a subquestion
Point value associations for the problem or subproblems, including extra credit points
Solutions, either typed or handwritten
Tables, diagrams, circuit schematics, or block diagrams
Your task is to identify and separate each exam problem into the listed components, including context, sub-questions, and solutions. If you encounter any images and tables, do not attempt to copy them. Instead, replace them with [IMAGE] or [TABLE] accordingly. Ignore any point values for any problem, question, or sub-question. Format your response using the template below. If the particular exam question lacks any of the listed components, do not include them.
Respond with the following Json format:
```json
[
  {
    "problem": <Copy the problem number and/or information>,
    "problem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>,
    "problem_figures": [Insert any images or tables (Tables, diagrams, circuit schematics, or block diagrams) pertaining to the general problem context only. If there are multiple figures, insert them as a list]
    "parts": [
      {
        "part": <Insert part number or letter, e.g., 1 or a. If no subproblem parts exist, just use the below question and solutions structure>,
        "question": [
          {
            "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header>,
            "subproblem_question": <Insert the full text of the question, exactly as it appears in the original>,
            "subproblem_figures": [Insert any images or tables (Tables, diagrams, circuit schematics, or block diagrams) pertaining to the subproblem context only. If there are multiple figures, insert them as a list]
            }
        ]
        "answer": [
          {
            "solution": <Insert the full solution exactly as shown in the original>,
            "solution_figures": [Insert any images or tables (Tables, diagrams, circuit schematics, or block diagrams) pertaining to the solution only. If there are multiple figures, insert them as a list]
          }
        ]
      }
      {
        "part": <Insert part number or letter, e.g., 1 or a. If no subproblem parts exist, just use the below question and solutions structure>,
        "question": [
          {
            "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header>,
            "subproblem_question": <Insert the full text of the question, exactly as it appears in the original>,
            "subproblem_figures": [Insert any images or tables (Tables, diagrams, circuit schematics, or block diagrams) pertaining to the subproblem context only. If there are multiple figures, insert them as a list]
            }
        ]
        "answer": [
          {
            "solution": <Insert the full solution exactly as shown in the original>,
            "solution_figures": [Insert any images or tables (Tables, diagrams, circuit schematics, or block diagrams) pertaining to the solution only. If there are multiple figures, insert them as a list]
          }
        ]
          // ...repeat as needed for additional Q&A pairs within this part
      }
    ]
    "problem": <Copy the problem number and/or information>,
    "problem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>,
    "problem_figures": [Insert any images or tables (Tables, diagrams, circuit schematics, or block diagrams) pertaining to the general problem context only. If there are multiple figures, insert them as a list]
    "parts": [
      {
        "part": <Insert part number or letter, e.g., 1 or a. If no subproblem parts exist, just use the below question and solutions structure>,
        "question": [
          {
            "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header>,
            "subproblem_question": <Insert the full text of the question, exactly as it appears in the original>,
            "subproblem_figures": [Insert any images or tables (Tables, diagrams, circuit schematics, or block diagrams) pertaining to the subproblem context only. If there are multiple figures, insert them as a list]
            }
        ]
        "answer": [
          {
            "solution": <Insert the full solution exactly as shown in the original>,
            "solution_figures": [Insert any images or tables (Tables, diagrams, circuit schematics, or block diagrams) pertaining to the solution only. If there are multiple figures, insert them as a list]
          }
        ]
      }
      {
        "part": <Insert part number or letter, e.g., 1 or a. If no subproblem parts exist, just use the below question and solutions structure>,
        "question": [
          {
            "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header>,
            "subproblem_question": <Insert the full text of the question, exactly as it appears in the original>,
            "subproblem_figures": [Insert any images or tables (Tables, diagrams, circuit schematics, or block diagrams) pertaining to the subproblem context only. If there are multiple figures, insert them as a list]
            }
        ]
        "answer": [
          {
            "solution": <Insert the full solution exactly as shown in the original>,
            "solution_figures": [Insert any images or tables (Tables, diagrams, circuit schematics, or block diagrams) pertaining to the solution only. If there are multiple figures, insert them as a list]
          },
        ]
          // ...repeat as needed for additional Q&A pairs within this part
      }
    ]
  }
]
Respond with valid JSON only.
"""

def signed_url_from_pdf(pdf_path):
    """
    Uploads a PDF file to Mistral and returns a signed URL for OCR processing.
    """
    uploaded_pdf = client.files.upload(
        file={
            "file_name": os.path.basename(pdf_path),
            "content": open(pdf_path, "rb"),
        },
        purpose="ocr"
    )  

    signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)
    return signed_url.url

def call_mistral(pdf_path):
    url = signed_url_from_pdf(pdf_path)
    full_prompt = prompt + f"\n\nHere is the PDF URL: {url}"
    resp = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": full_prompt},
        ],
        max_tokens=2000,
    )
    return resp.choices[0].message.content
    
    return chat_response.choices[0].message.content

def list_pdf_files(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path)
            if f.lower().endswith('.pdf')]

def main(in_folder, output_file): #no img_folder yet, implement later
    results = []
    for pdf_path in list_pdf_files(in_folder):
        try:
            res = call_mistral(pdf_path)
            results.append(res)
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
    # Write to JSON file
    
    with open(output_file, 'w', encoding='utf-8') as out:
        json.dump(results, out, ensure_ascii=False, indent=2)
    #     out.write(str(results))
    print(f"Classified {len(results)} problems. Output saved to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Classify pdf problems using Mistral AI")
    parser.add_argument('in_folder', help="Path to exam file (PDF)")
    #parser.add_argument('img_folder', help="Path to folder with images") not yet image compatible
    parser.add_argument('-o', '--output', default='classified_problems.json',
                        help="Output JSON filename")
    args = parser.parse_args()

    main(args.in_folder, args.output)


