import os, json, boto3
from botocore.exceptions import ClientError
from botocore.config import Config
import helper

config = Config(read_timeout=1000)
client = boto3.client("bedrock-runtime", region_name="us-east-2", config=config)


# Takes in an individual exam json and accuracy-checks it
def process(json_path, extracted_problems_folder, images_folder):
    filename = os.path.basename(json_path)[14:-5]
    print("Verifying Accuracy via Claude 3.7: ", filename)
    verified_output = [] # Final output of the verification process: the altered json

    prompt = """
    Attached are images, parts of a problem (context, question, and solution) separated into a JSON Format, and a pdf of the original problem. Your task is to determine if the images were extracted faithfully from the original problem. 

Reference the PDF to determine the completeness of the image. For example, the image should not be cut or cropped, split into two separate images, and should not omit any labels or arrows relevant to it.

Your output should be a modified version of the given json dictionary. The new dictionary's "passed_llm_image_verification" fields should now be all changed to either true (if the question has been correctly parsed) or false (if  any of the above conditions are not satisfied), without quotation marks. 

For each question marked false, the dictionary should include your reasoning for it in a new field called "image_reasoning".

Only ouput one dictionary and nothing else. 
 
You should err on the side of classifying more image-based problems as false rather than true; in other words, there should be no false positives (marking an incorrectly parsed question as true), while false negatives are allowed (marking a correctly parsed question as false).

    """


    with open(json_path, "r") as exam_json:
        full_exam = json.loads(exam_json.read())

    for problem_pdf in os.listdir(os.path.join(extracted_problems_folder, filename)):
        # Read in the PDF as bytes
        with open(os.path.join(extracted_problems_folder, filename, problem_pdf), "rb") as pdf:
            pdf_bytes = pdf.read()

        # From the full exam json, grab only the questions parsed from that problem
        for question in full_exam:
            problem_dict = []
            images = []

            if problem_pdf[:-4] == question["question_id"].split("/")[1]:
                 # Add new "passed_human_verification" field
                question["passed_human_verification"] = None
                
                problem_dict.append(question)

                # If there are no images..
                if not question["context_figures"] and not question["solution_figures"]:
                    question["passed_llm_image_verification"] = True
                
                # If there are context figures or solution figures present... 
                else:
                    # Keep track of images associated
                    images += question["context_figures"] + question["solution_figures"]

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

                # #Create a new json file for the checked/verified version
                # verified_filepath = os.path.join("image_testing_out", "[IMAGE_CHECKED]" + filename + ".json") 
                # with open(verified_filepath, 'w') as file:
                #     json.dump(verified_output, file, indent=4)
                        
                            
        print("problem dict ", problem_dict)

        

folder = "auto checked"
for exam_json in os.listdir(folder):
    if exam_json.endswith(".json"):
        process(os.path.join(folder, exam_json), "extracted_problems", "images")

    
