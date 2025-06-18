import boto3
import json
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-2")

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