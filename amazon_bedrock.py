import boto3
import json
from botocore.exceptions import ClientError

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
query_prompt = "Are there an infinite number of prime numbers such that n mod 4 == 3?"

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
            "content": query_prompt
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
            "content": query_prompt
        }
    ]
}

response_claude_non_thinking = invoke_model(claude_inference_profile_arn, claude_non_thinking_payload)
print("\n=== Claude 3.7 Sonnet Without Thinking ===")
print(response_claude_non_thinking)

#########################################
# 2. Inference for Meta Llama3 2-90B Instruct
#########################################

llama_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.meta.llama3-2-90b-instruct-v1:0"

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
}

response_llama = invoke_model(llama_inference_profile_arn, llama_payload)
print("\n=== Meta Llama3 2-90B Instruct ===")
print(response_llama)

#########################################
# 3. Inference for Deepseek R1
#########################################

deepseek_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/DeepseekProfile"

deepseek_payload = {
    "prompt": query_prompt,
    "max_tokens": 512,
    "temperature": 0.5,
}

response_deepseek = invoke_model(deepseek_inference_profile_arn, deepseek_payload)
print("\n=== Deepseek R1 ===")
print(response_deepseek)