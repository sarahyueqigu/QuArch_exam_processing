##############
#Using the AWS Bedrock API, we call various other LLMs to verify the output problem json files
##############

#input: the .json file of the main pipeline output, the original exam pdf file, and the problem image folder corresponding to that exam

#output, each llm should return a dict with N entries (the number of total problems in the exam), where each entry is either "yes" or "no" depending on if the problem was parsed correctly.

import boto3
import json
import base64
from botocore.exceptions import ClientError
import os

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-2")

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

# Define the common query prompt.

## work in progress prompt:
query_prompt = """
You are a language model tasked with identifying if problems from a computer architecture exam have been correctly parsed into a json format with the keys in the following forms: 
"question_id": "exam_name/Problem_number/subproblem_letter" (e.g. "a", "b", etc.), 
"context": "<Insert any introductory paragraph or description exactly as it appears. If there is no context, don’t include this header>", 
"context_figures": "file_directory_path/exam_name/img_number",
"question": "<Insert the full question of the problem, exactly as it appears in the original>", 
"solution": "<Insert the full solution of the problem, exactly as shown in the original>", 
"solution_figures": "file_directory_path/exam_name/img_number",
"correctly_parsed": "null" (indicating if the problem was parsed correctly).
You will be given a json file with the parsed problems, the original exam pdf file, and the problem image folder corresponding to that exam. 
Return the same json dict with the "correctly_parsed" field filled in with either the boolean true or false.
If the problem was parsed correctly, return true, otherwise return false. 
Return only valid json.
"""

#########################################
# 1. Inference for Anthropic Claude 3.7 Sonnet
#########################################

claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"
# --- A. With Thinking Enabled ---
# /Users/aliceguo/Documents/QuArch_exam_processing/output/exam_solutions_ss2012.json
root_dir = "exams"

def load_file_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def make_images_payload(image_dir):
    images_payload = []
    for fname in os.listdir(image_dir):  
        if fname.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            fullp = os.path.join(image_dir, fname)
            with open(fullp, "rb") as img:
                images_payload.append({
                    "filename": fname,
                    "data": img.read()
                })
    return images_payload

def claude_veri(pdf_path, image_path, json_path):
    #old params: claude_veri(pdf_path, pdf_b64, image_payload, json_payload) #want to do for all pdf_name in root_dir, we run this api verification call
    claude_thinking_payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 24000,
        "thinking": {
            "type": "enabled",
            "budget_tokens": 1500
        },
        "messages": [
            {
                "role": "user",
                "content": query_prompt
            }
        ],
        "attachments": {
            "pdf": {
                "filename": os.path.basename(pdf_path),
                "data": pdf_b64
            },
            "images": images_payload,
            "json_data": json_payload
        }
    }
    #print response just in case(and for debugging)
    #response_claude_thinking = invoke_model(claude_inference_profile_arn, claude_thinking_payload) 7/14 old thing
    images = make_images_payload(image_path)  # Assuming images are in a folder named "exam_images"
    response_claude_thinking = client.converse(
    modelId=claude_inference_profile_arn,
    messages=[{"role": "user", "content": query_prompt}],
    attachments=[
        {"filename": pdf_path, "bytes": open(pdf_path, "rb").read()},
        images,
        {"filename": json_path, "bytes": open(json_path, "rb").read()}
        # {"filename": "q1.png",  "bytes": open(img_path, "rb").read()},
    ],
    contentType="application/json",
    accept="application/json",
)   #The above uses the converse api, which should allow direct upload/reading of pdf files
    print("=== Claude 3.7 Sonnet With Thinking ===")
    print(response_claude_thinking)

    #print out to json file
    with open("claude_response.json", "w", encoding="utf-8") as out:
        json.dump(response_claude_thinking, out, indent=2, ensure_ascii=False)

    print("Response saved to claude_response.json")

# # --- B. With Thinking Disabled ---
# claude_non_thinking_payload = {
#     "anthropic_version": "bedrock-2023-05-31",
#     "max_tokens": 24000,
#     "thinking": {
#         "type": "disabled"
#     },
#     "messages": [
#         {
#             "role": "user",
#             "content": query_prompt
#         }
#     ]
# }

# response_claude_non_thinking = invoke_model(claude_inference_profile_arn, claude_non_thinking_payload)
# print("\n=== Claude 3.7 Sonnet Without Thinking ===")
# print(response_claude_non_thinking)

#########################################
# 2. Inference for Meta Llama3 2-90B Instruct
#########################################

llama_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.meta.llama3-2-90b-instruct-v1:0"

def llama_veri(pdf_path, pdf_b64, images_payload, json_payload):
    llama_prompt = (
        "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n"
        f"{query_prompt}\n"
        "<|eot_id|>\n"
        "<|start_header_id|>assistant<|end_header_id|>"
    )
    llama_payload = {
        "prompt": llama_prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "attachments": {
                "pdf": {
                    "filename": os.path.basename(pdf_path),
                    "data": pdf_b64
                },
                "images": images_payload,
                "json_data": json_payload
        }
    }

    response_llama = invoke_model(llama_inference_profile_arn, llama_payload)
    print("\n=== Meta Llama3 2-90B Instruct ===")
    print(response_llama)

    #print out to json file
    with open("llama_response.json", "w", encoding="utf-8") as out:
        json.dump(response_llama, out, indent=2, ensure_ascii=False)

    print("Response saved to llama_response.json")

#########################################
# Mistral AI Pixtrel Large
#########################################
def mistral_veri(pdf_path, pdf_b64, images_payload, json_payload):
    mistral_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.mistral.pixtral-large-2502-v1:0"
    mistral_payload = {
        "prompt": query_prompt,
        "max_tokens": 24000,
        "temperature": 0.5,
        "attachments": {
                    "pdf": {
                        "filename": os.path.basename(pdf_path),
                        "data": pdf_b64
                    },
                    "images": images_payload,
                    "json_data": json_payload
            }
    }
    response_mistral = invoke_model(mistral_inference_profile_arn, mistral_payload)
    print("\n=== Mistral AI Pixtrel Large ===")
    print(response_mistral)

    #print out to json file
    with open("llama_response.json", "w", encoding="utf-8") as out:
        json.dump(response_mistral, out, indent=2, ensure_ascii=False)

    print("Response saved to mistral_response.json")



# ########################################
# 3. Inference for Deepseek R1v
# ########################################

deepseek_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/DeepseekProfile"

def deepseek_veri(pdf_path, pdf_b64, images_payload, json_payload):
    deepseek_payload = {
        "prompt": query_prompt,
        "max_tokens": 512,
        "temperature": 0.5,
        "attachments": {
                        "pdf": {
                            "filename": os.path.basename(pdf_path),
                            "data": pdf_b64
                        },
                        "images": images_payload,
                        "json_data": json_payload
                }
    }

    response_deepseek = invoke_model(deepseek_inference_profile_arn, deepseek_payload)
    print("\n=== Deepseek R1 ===")
    print(response_deepseek)

    #print out to json file
    with open("llama_response.json", "w", encoding="utf-8") as out:
        json.dump(response_deepseek, out, indent=2, ensure_ascii=False)

    print("Response saved to deepseek_response.json")


#============================main===========================
if __name__ == "__main__":
    root_dir = "verification_test" #"exams" for all the exams, put the file directory path of the folder with the pdfs of the exams
    for pdf_name in os.listdir(root_dir):
        pdf_name = pdf_name.split(".")[0]  # Remove file extension
        pdf_path = os.path.join(root_dir, pdf_name + ".pdf")  # Assuming the PDF files are named like "exam_name.pdf"
        pdf_b64 = load_file_base64(pdf_path)
        image_path = os.path.join("images", pdf_name)   
        images_payload = make_images_payload(image_path)
        json_path = os.path.join("output", pdf_name + ".json")   
        with open(json_path, "r") as f:
            json_payload = json.load(f)
        print(f"Processing {pdf_name}...")
        #old verification calls with old parameters
        #claude_veri(pdf_path, pdf_b64, images_payload, json_payload)    
        #llama_veri(pdf_path, pdf_b64, images_payload, json_payload)   
        # mistral_veri(pdf_path, pdf_b64, images_payload, json_payload)    
        # deepseek_veri(pdf_path, pdf_b64, images_payload, json_payload)

        claude_veri(pdf_path, image_path, json_path)  # Using the new converse API
        