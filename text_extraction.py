import boto3
from botocore.exceptions import ClientError
import config
import os
import json
import image_identifying
from botocore.config import Config
import helper

config = Config(read_timeout=1000)
client = boto3.client("bedrock-runtime", region_name="us-east-2", config=config)

def claud_37_processing(path, arn):
    filename = os.path.basename(path)[:-4]

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
    Format your response so that it can be exported into a JSON file using the template below. 
    If the particular exam question lacks any of the listed components, omit them from the template.

    Template for a problem which is split up into sub-problems:
    {{
      "problem": "1",
      "problem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>,
      "subproblems": [ 
        {{
          "subproblem": "a" (Copy the part letter/number exactly as it appears on the exam),
          "subproblem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no subproblem context or if the question is the only part of the subproblem, don’t include this header. Replace all double quotes " here with escaped double quotes /">,
          "subproblem_question": <Insert the full question of the subproblem, exactly as it appears in the original. Replace all double quotes " here with escaped double quotes /">,
          "subproblem_solution": <Insert the full solution of the subproblem, exactly as shown in the original. Replace all double quotes " here with escaped double quotes /">
        }},
        ...repeat as needed for additional subproblems within this problem
      ],
    }}

    Template for a problem which is standalone and has no sub-problems:
    {{
      "problem": "1",
      "problem_context": <Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header. Replace all double quotes " here with escaped double quotes /">,
      "problem_question": <Insert the full question of the problem, exactly as it appears in the original. Replace all double quotes " here with escaped double quotes /">,
      "problem_solution": <Insert the full solution of the problem, exactly as shown in the original. Replace all double quotes " here with escaped double quotes /">
    }}

    If any double quotes (") within strings appear within your JSON, you must replace them with escaped double quotes (/").
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
            modelId=arn,
            messages=conversation,
            inferenceConfig={"maxTokens": 4000, "temperature": 0},
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        #print(response_text)
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{arn}'. Reason: {e}")
        exit(1)


def process(file_path, pages_data, arn, api): # pages_data is the dictionary from problem_page_extraction that defined each problem's page range

  print("\nTEXT_EXTRACTION")
  filename = os.path.basename(file_path)[:-4]
  problems_path = os.path.join("extracted_problems", filename)
  output = []

  # Create folder structure for this
  parent_folder = "out_model_comparison/" + filename
  os.makedirs(parent_folder, exist_ok= True)
  output_path = os.path.join(parent_folder, api + ".json")
  
  for problem in os.listdir(problems_path):
      print("Processing text in:", problem)
      json_text = claud_37_processing(os.path.join(problems_path, problem), arn)
      stripped_json = helper.strip_json_code_block(json_text)
      print("Raw problem output: ", stripped_json)
      problem_dict = json.loads(stripped_json) # This is the extracted problem text in json format

      # Prep problem_dict with empty "figures" fields, which image_identifying will fill in
      if problem_dict.get("subproblems") != None: # if there are subproblems    
          problem_dict["problem_context_figures"] = []
          for subproblem in problem_dict["subproblems"]:
            subproblem["subproblem_context_figures"] = []
            subproblem["subproblem_solution_figures"] = [] 
      else:
          problem_dict["problem_context_figures"] = []
          problem_dict["problem_solution_figures"] = []

      # First identify the associated images with the problem
      # If there are no images, don't call image_identifying
      if len(pages_data[problem[:-4]]) > 2:
        images = pages_data[problem[:-4]][2:]

        # Call image_identifying for each problem, feeding it:
        # 1) original problem PDF, 2) problem json, 3) associated images
        problem_with_imgs = json.loads(strip_json_code_block(image_identifying.process(filename, os.path.join(problems_path, problem), problem_dict, images)))
        # TODO: make image_identifying an async function? to speed things up
      else:
         problem_with_imgs = problem_dict

      #Deconstruct the json into standalone QA pairs
      problem_output = {}  # we will later append this to output
      if problem_with_imgs.get("subproblems") != None: # if there are subproblems
        for subproblem in problem_with_imgs["subproblems"]:
            subproblem_output = {}
            subproblem_output["question_id"] = filename + "/" + problem[:-4] + "/" + subproblem.get("subproblem", "")             
            # Ensure main problem context is included
            subproblem_output["context"] = problem_with_imgs.get("problem_context", "") + "\n" + subproblem.get("subproblem_context", "")
            subproblem_output["context_figures"] = problem_with_imgs.get("problem_context_figures", []) + subproblem.get("subproblem_context_figures", [])
            subproblem_output["question"] = subproblem.get("subproblem_question", "")
            subproblem_output["solution"] = subproblem.get("subproblem_solution", "")
            subproblem_output["solution_figures"] = problem_with_imgs.get("problem_solution_figures", []) + subproblem.get("subproblem_solution_figures", [])
            subproblem_output["correctly_parsed"] = None
            problem_output[subproblem["subproblem"]] = subproblem_output

      else: # if this is a standalone question
        problem_output["problem"] = {
          "question_id" : filename + "/" + problem[:-4],
          "context" : problem_with_imgs.get("problem_context", ""),
          "context_figures" : problem_with_imgs.get("problem_context_figures", []),
          "question" : problem_with_imgs.get("problem_question", ""),
          "solution" : problem_with_imgs.get("problem_solution", ""),
          "solution_figures" : problem_with_imgs.get("problem_context_figures", []),
          "correctly_parsed" : None
      }

      print("Problem Output: ", problem_output)

      # Now add all these questions to the final out object
      for key in problem_output:
          
          # Write all the data into an intermediary folder
          preprocessed_output = os.path.join("preprocessed_output", filename)
          os.makedirs(preprocessed_output, exist_ok = True)

          with open(preprocessed_output + "/" + problem + ".json", 'w') as file:
            json.dump(problem_dict, file, indent=4)
          
          # Add this data to a larger json file
          output.append(problem_output[key])

  # Write all problems to the final json
  with open(output_path, 'w') as file:
    json.dump(output, file, indent=4)
      
