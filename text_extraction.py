import boto3
from botocore.exceptions import ClientError
import os
import json

client = boto3.client("bedrock-runtime", region_name="us-east-2")


def claud_37_processing(path):
    filename = os.path.basename(path)[:-4]
    claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"

    prompt = """You are a language model assisting with the digitization of academic exam content. The input is a PDF file containing one problem of a Computer Architecture Assessment. If part of another problem is included, ignore it and only focus on {filename}. 
    The problem may include any combination of the following:
    A context paragraph, or just a short statement (e.g., “Convert the number 42 to binary”)
    One or more sub-questions, or be a single standalone question
    Context for sub-questions separate from the sub-question and separate from the original problem context
    Multiple questions within a subquestion
    Point value associations for the problem or subproblems, including extra credit points
    Solutions, either typed or handwritten
    Tables, diagrams, circuit schematics, or block diagrams

    Your task is to identify and separate each exam problem into the listed components, including context, sub-questions, and solutions. At times, a subquestion can have nested subparts. Ignore any point values for any problem, question, or sub-question. Ignore any images, charts, or figures and do not attempt to extract text from them. 
    If a provided image is not part of {filename} and instead is part of another problem(s), omit it from the dictionary.
    Format your response so that it can be exported into a JSON file using the template below. If the particular exam question lacks any of the listed components, omit them from the template.

    Template for a problem which is split up into sub-problems:
    {{
      "problem": "1",
      "problem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>,
      "subproblems": [ 
        {{
          "subproblem": "a",
          "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header>,
          "subproblem_question": <Insert the full question of the subproblem, exactly as it appears in the original>,
          "subproblem_solution": <Insert the full solution of the subproblem, exactly as shown in the original>
        }},
        ...repeat as needed for additional subproblems within this problem
      ],
    }}

    Template for a problem which is standalone and has no sub-problems:
    {{
      "problem": "1",
      "problem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>,
      "problem_question": <Insert the full question of the problem, exactly as it appears in the original>,
      "problem_solution": <Insert the full solution of the problem, exactly as shown in the original>
    }}
    """.format(filename = filename)
    
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
            inferenceConfig={"maxTokens": 4000, "temperature": 0.3},
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        #print(response_text)
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{claude_inference_profile_arn}'. Reason: {e}")
        exit(1)


def strip_json_code_block(text: str) -> str:
    # find the first “{” and the last “}”
    start = text.index("{")
    end   = text.rindex("}") + 1
    text2 = text[start:end]
    
    # Remove opening and closing code block markers
    lines = text2.strip().splitlines()
    cleaned_lines = [line for line in lines if not line.strip().startswith("```")]
    return "\n".join(cleaned_lines)




def process(file_path, matches):
  print("\nTEXT_EXTRACTION")
  filename = os.path.basename(file_path)[:-4]
  problems_path = os.path.join("extracted_problems", filename)
  output = [] # List of all problems separated, will be pushed to final json

  for problem in os.listdir(problems_path):
      # Only process the problem PDFs, ignore the images folder
      if problem.lower().endswith(".pdf"):
        print("Processing text in:", problem)
        json_text = claud_37_processing(os.path.join(problems_path, problem))
        stripped_json = strip_json_code_block(json_text)
        print(stripped_json)
        problem_dict = json.loads(stripped_json)

        problem_output = {}  # we will later append this to output
        #Deconstruct the json into standalone QA pairs
        if problem_dict.get("subproblems") != None: # if there are subproblems
          for subproblem in problem_dict["subproblems"]:
              subproblem_output = {}
              subproblem_output["question_id"] = filename + "/" + problem[:-4] + "/" + subproblem.get("subproblem", "")             # Ensure main problem context is included
              subproblem_output["context"] = problem_dict.get("problem_context", "") + "\n" + subproblem.get("subproblem_context", "")
              subproblem_output["context_figures"] = []
              subproblem_output["question"] = subproblem.get("subproblem_question", "")
              subproblem_output["solution"] = subproblem.get("subproblem_solution", "")
              subproblem_output["solution_figures"] = []
              subproblem_output["correctly_parsed"] = None
              problem_output[subproblem["subproblem"]] = subproblem_output

        else: # if this is a standalone question
          problem_output["problem"] = {
            "question_id" : filename + "/" + problem[:-4],
            "context" : problem_dict.get("problem_context", ""),
            "context_figures" : [],
            "question" : problem_dict.get("problem_question", ""),
            "solution" : problem_dict.get("problem_solution", ""),
            "solution_figures" : [],
            "correctly_parsed" : None
          }

        # Insert correct images using the 'matches' dictionary
        for figure in matches.get(problem, []):
            figure_path = os.path.join("images", filename, figure["name"])
            # Add main-context & main-solution figures to ALL problems/subproblems
            if figure["type"] == "problem_figure":
              for key in problem_output:
                problem_output[key]["context_figures"].append(figure_path)
            elif figure["type"] == "problem_solution":
              for key in problem_output:
                problem_output[key]["solution_figures"].append(figure_path)
            # Add subproblem-specific figures to only that subproblem
            elif figure["type"] == "subproblem_figure":
              problem_output[figure["part"]]["context_figures"].append(figure_path)
            elif figure["type"] == "subproblem_solution":
              problem_output[figure["part"]]["solution_figures"].append(figure_path)

        print(problem_output)
        # Now add all these questions to the final out object
        for key in problem_output:
            output.append(problem_output[key])
        
    
  with open(os.path.join(problems_path, filename + ".json"), 'w') as file:
    json.dump(output, file, indent=4)
    
    
  


