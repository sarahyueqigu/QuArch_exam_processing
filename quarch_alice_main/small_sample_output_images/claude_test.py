<<<<<<< Updated upstream
import boto3
import json
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-2")

prompt = """
=======
#not outputting anything, do we not have access to claude sonnet 3.7 or 4?
from __future__ import annotations  
import boto3
import json
import base64
import io
import pymupdf
from PIL import Image
from botocore.exceptions import ClientError
#from pdf2image import convert_from_bytes

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-2")
modelId4="anthropic.claude-sonnet-4-20250514-v1:0"

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

def get_file_bytes(file_path: str) -> bytes:
    """Read a file (PDF) from disk and return its raw bytes."""
    with open(file_path, "rb") as f:
        return f.read()
#Using pdf2image and poppler, which i have downloaded anyway lmao
# def split_pdf_to_images(pdf_bytes: bytes,
#                         fmt: str = "png",
#                         max_size: tuple[int, int] = (1024, 1024)
#                        ) -> list[str]:
#     """
#     Convert each PDF page to an image, resize if too large, 
#     and return a list of base64-encoded PNG strings.
#     """
#     images = convert_from_bytes(pdf_bytes, fmt=fmt)
#     encoded_pages = []
#     for img in images:
#         # down-scale pages exceeding max_size
#         if img.width > max_size[0] or img.height > max_size[1]:
#             img.thumbnail(max_size)
#         buf = io.BytesIO()
#         img.save(buf, format=fmt.upper())
#         encoded_pages.append(base64.b64encode(buf.getvalue()).decode("utf-8"))
#     return encoded_pages

#Using pymupdf
def split_pdf_to_images(pdf_bytes, fmt="png", max_size=(1024,1024)):
    doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
    encoded = []
    for page in doc:
        pix = page.get_pixmap()
        # get a full PNG raster stream directly:
        png_bytes = pix.tobytes("png")
        img = Image.open(io.BytesIO(png_bytes))
        if img.width > max_size[0] or img.height > max_size[1]:
            img.thumbnail(max_size)
        buf = io.BytesIO()
        img.save(buf, format=fmt.upper())
        encoded.append(base64.b64encode(buf.getvalue()).decode())
    return encoded

def build_claude_payload_with_pdf(pdf_path: str,
                                  user_prompt: str,
                                  anthropic_version: str = "bedrock-2023-05-31",
                                  max_tokens: int = 24000,
                                  thinking_budget: int = 1500
                                 ) -> dict:
    """
    Construct the JSON payload for Claude, embedding each PDF page as a base64 image,
    followed by the text prompt.
    """
    pdf_bytes = get_file_bytes(pdf_path)
    b64_images = split_pdf_to_images(pdf_bytes)

    # build the mixed ‘content’ list
    content = [
        {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": img_data
            }
        }
        for img_data in b64_images
    ]
    # finally append your text prompt
    content.append({"type": "text", "text": user_prompt})

    return {
        "anthropic_version": anthropic_version,
        "max_tokens": max_tokens,
        "thinking": {
            "type": "enabled",
            "budget_tokens": thinking_budget
        },
        "messages": [
            {"role": "user", "content": content}
        ]
    }

# --- Usage ---

claude_inference_profile_arn4 = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0"
claude_inference_profile_arn3_7 = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"
query_prompt = """
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
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



#########################################
# 1. Inference for Anthropic Claude 3.7 Sonnet
#########################################

claude_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0"
# --- A. With Thinking Enabled ---
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
            "content": prompt
        }
    ]
}

response_claude_thinking = invoke_model(claude_inference_profile_arn, claude_thinking_payload)
print("=== Claude 3.7 Sonnet With Thinking ===")
print(response_claude_thinking)

# --- B. With Thinking Disabled ---
claude_non_thinking_payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 24000,
    "thinking": {
        "type": "disabled"
    },
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}
=======
# Build a payload that includes the PDF
payload_with_pdf = build_claude_payload_with_pdf("/Users/aliceguo/Documents/QuArch_exam_processing/quarch_alice_main/small_sample_exams/2001-spring-final-sol.pdf", query_prompt)

# Invoke Claude with both the PDF pages and your prompt
response = invoke_model(claude_inference_profile_arn3_7, payload_with_pdf)
print(json.dumps(response, indent=2))
>>>>>>> Stashed changes
