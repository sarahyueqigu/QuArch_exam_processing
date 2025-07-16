import os, json, boto3
from botocore.exceptions import ClientError
from botocore.config import Config
import helper

config = Config(read_timeout=1000)
client = boto3.client("bedrock-runtime", region_name="us-east-2", config=config)


# Takes in an individual exam json and accuracy-checks it
def process(json_path, extracted_problems_folder, images_folder):
    filename = os.path.basename(json_path)[:-5]
    print("Verifying Accuracy via Claude 3.7: ", filename)
    verified_output = [] # Final output of the verification process: the altered json

    prompt = """
    You are a reader tasked with verifying the accuracy of an automated document parser. A computer architecture exam PDF has been fed through the parser to produce standalone question-answer pairs in a certain json format, and you must compare the parsed questions to the original questions in the PDF. 

    Input: You are given 1) the original PDF of {problem_name} of the exam which may be broken down into subproblems, 2) the json dictionary produced by the parser, and 3) images that the parser has deemed are associated with the question and/or its subproblems. The names of the images provided are as follows, in order: {images}
    Your task is to determine if the parser has correctly extracted the text and images while staying true to the original PDF. 
    The following conditions must be satisfied in order for a problem to be deemed as correct:

    a) The extracted problem text is nearly identical, word-for-word, to the original PDF's text, with the exception of special characters or math symbols which should still be included as unicode escaped characters or some other representation.
    b) The problem's "question" and "solution" fields are both populated. The only exceptions are if the solution from the original PDF consists purely of an image, in which case the image should correctly be associated with the problem, and the "solution_figures" field must contain the name of that image.
    c) The problem is standalone, meaning that it contains all the context (in the "context" and "context_figures" fields) information that a student would need to complete the problem. 
    d) No part of the solution to the problem is revealed in the "context" field or in any of the images referenced in the "context_figures" field.
    e) All images are extracted and cropped correctly, and each is categorized correctly as a context figure versus a solution figure
    f) All tables are extracted correctly, whether as text or as an associated context or solution figure. If a table is in the original question PDF and is only parsed in text rather than image form, 
    it must be recreatable from the extracted text and then usable by a student to answer the question. 
    g) For fill-in-the-blank or fill-in-the-chart questions, the original blank version must be provided in the context/question or context figures. 

    Your output should be a modified version of the given json dictionary. The new dictionary's "passed_llm_verification" fields should now be all changed to either true (if the question has been correctly parsed) or false (if  any of the above conditions are not satisfied), without quotation marks. 
    For each question marked false, the dictionary should include your reasoning for it in a new field called "reasoning".
    Only ouput one dictionary and nothing else. 
    You should err on the side of classifying more problems as false rather than true; in other words, there should be no false positives (marking an incorrectly parsed question as true), while false negatives are allowed (marking a correctly parsed question as false).
    """


    with open(json_path, "r") as exam_json:
        full_exam = json.loads(exam_json.read())

    for problem_pdf in os.listdir(os.path.join(extracted_problems_folder, filename)):
        # Read in the PDF as bytes
        with open(os.path.join(extracted_problems_folder, filename, problem_pdf), "rb") as pdf:
            pdf_bytes = pdf.read()

        # From the full exam json, grab only the questions parsed from that problem
        problem_dict = []
        images = []
        for question in full_exam:
            if problem_pdf[:-4] == question["question_id"].split("/")[1]:
                 # Add new "passed_human_verification" field
                question["passed_human_verification"] = None
                problem_dict.append(question)

                # Also keep track of images associated
                images += question["context_figures"] + question["solution_figures"]
        print("problem dict ", problem_dict)

        # Read in the new sub-dictionary as bytes
        json_bytes = json.dumps(problem_dict, indent=4).encode('utf-8')


        # Start a conversation with a user message and the document
        conversation = [
            {
                "role": "user",
                "content": [
                    {"text": prompt.format(problem_name = problem_pdf[:-4], images=images)},
                    {
                        "document": {
                            # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                            "format": "pdf",
                            "name": "Computer Architecture Exam Problem PDF",
                            "source": {"bytes": pdf_bytes},
                        }
                    },
                    {
                        "document": {
                            # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                            "format": "txt",
                            "name": "Problem json File",
                            "source": {"bytes": json_bytes},
                        }
                    }
                ],
            }
        ]

        # Add all image files to the conversation
        for image in images:
            image_path = os.path.join(images_folder, filename, image)
            with open(image_path, "rb") as image_file:
                image_bytes = image_file.read()
            # Append image to conversation
            conversation[0]["content"].append(
            {
                "image": {
                    "format": "png",
                    "source": {
                        "bytes": image_bytes 
                    }
                }
            }
            )    
    
        claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"

        try:
            # Send the message to the model, using a basic inference configuration.
            response = client.converse(
                modelId=claude_inference_profile_arn,
                messages=conversation,
                inferenceConfig={"maxTokens": 10000, "temperature": 0.0},
            )

            # Extract and print the response text.
            response_text = response["output"]["message"]["content"][0]["text"]
            print("Json Returned by Verifier: ", response_text)

            # Add the modified dictionaries to final output 
            verified_output += json.loads(helper.string_to_list(response_text))


        except ClientError as e:
            print(f"CLIENT ERROR: Can't invoke '{claude_inference_profile_arn}'. Reason: {e}")
            exit(1)
        except Exception as e:
            print(f"EXCEPTION: {e}")
            exit(1)

    #Create a new json file for the checked/verified version
    verified_filepath = os.path.join("out", "[AUTO_CHECKED]" + filename + ".json") 
    with open(verified_filepath, 'w') as file:
        json.dump(verified_output, file, indent=4)
            

for exam_json in os.listdir("out"):
    # Only check the ones that have not been checked yet
    if "[AUTO_CHECKED]"+exam_json not in os.listdir("out"):
        process(os.path.join("out", exam_json), "extracted_problems", "images")

    
