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
<<<<<<< Updated upstream
query_prompt = "Are there an infinite number of prime numbers such that n mod 4 == 3?"
#"You are a language model assisting with the digitization of academic exam content. The input is an exam which has been parsed into Markdown text. The exam contains one or more problems from a Computer Architecture assessment. A problem may include any combination of the following: A context paragraph, or just a short statement (e.g., “Convert the number 42 to binary”) One or more sub-questions, or be a single standalone question Context for sub-questions separate from the sub-question and separate from the original problem context Multiple questions within a subquestion Point value associations for the problem or subproblems, including extra credit points Solutions, either typed or handwritten, Tables, diagrams, circuit schematics, or block diagrams Your task is to identify and separate each exam problem into the listed components, including context, sub-questions, figures, and solutions. Ignore any point values for any problem, question, or sub-question. Format your response using the template below. If the particular exam question lacks any of the listed components, do not include them.## Problem Number Problem Context: <Fill in here> Sub-question 1. Sub-question context: <Fill in here> Figure context: <Fill in here> Question: <Fill in here> Solution: <Fill in here> Sub-question 2. Sub-question context: <Fill in here>  Figure context: <Fill in here> Question: <Fill in here> Solution: <Fill in here> The Document's text is: Q1. Single-Cycle MIPS Processor We wish to add the instruction jalr (jump and link register) to the single-cycle datapath. The jump and link register instruction is described below: jalr rd, rs # rd = pc + 4 , pc = rs op6 = 0 rs5 0 rd5 0 Funct6 = 0x9 a) Add any necessary datapath and control signals and draw the result datapath.  You should only add wires, gates, muxes to the datapath; do not modify the main functional units (the memory, register file, and ALU) themselves. Try to keep your diagram neat! The necessary changes to the datapath and control: For   the   datapath,   we   need   a   bigger   4­input   multiplexer   at   the input of the PC. The first input is used to increment the PC. The second input is used for taken branches, where the branch target is PC­relative. The third input is used to jump register, where the input to the PC comes from a general­purpose register, and the fourth input is used for jump instructions. For   the   implementation   of   the   JALR   instruction:   to   jump   to register ‘Rs’, we need to add a path from the output of register Rs (first ALU input) back to the PC multiplexer input. PC control unit needs to be updated by adding an input control signal JReg (Jump Register) to select PC according to the value of register Rs. JReg is generated by the ALU control unit, since JALR is a R­ 1 type instruction and JReg depends on the function field only. When JReg   is   equal   to   ‘1’,   PCSrc   (PC   control   unit   output   control signal) will be '10' to select the value of register Rs as input to PC. Also, we need to store PC+4 in register Rd. To accomplish this, we need another multiplexer to select between the incremented PC, the ALU result and data memory out, to be placed on BusW. Also, we need to add a path from the output of the incremented PC to the input   of   this   new   multiplexer.   A   control   signal   ‘RA’   (Return Address) is needed to select between the incremented PC and the ALU result. The MemtoReg multiplexer selects between the output of the ‘RA’ multiplexer and the Data Memory output to place on BusW. b) Show the values of the control signals to control the execution of the jalr instruction. If you need add a new control signal, please add it along with its value to the table below. Use the following table for ALUCtrl. ALU function 4-bit ALU Control AND 0001 OR 0010 XOR 0011 ADD 0100 SUB 0101 SLT 0110 The main control signals for the JALR instruction are the same for other R­type instructions, such as ADD and SUB. The ALU Control signals for the JALR instruction require JReg = 1, RA = 0 and ALUCtrl is a don't care. These control signals are shown in the table below: RegDs t RegWrit e ExtO p ALUSr c MemRead MemWrite MemtoReg ALUCtr l J Be q Bn e R A JRe g Rd = 1 1 X X 0 0 0 XXXX 0 0 0 0 1 Q2. Processor Performance Suppose we add the multiply and divide instructions. The operation times are as follows: Instruction memory access time = 190 ps,      Data memory access time = 190 ps, Register file read access time = 150 ps,   Register file write access = 150 ps ALU delay for basic instructions = 190 ps,      ALU delay for multiply or divide = 550 ps Ignore the other delays in the multiplexers, control unit, sign-extension, etc. 2 Assume the following instruction mix: 30% ALU, 15% multiply & divide, 20% load, 10% store, 15% branch, and 10% jump. a) What is the total delay for each instruction class and the clock cycle for the single- cycle CPU design? Clock cycle = max delay = 1040 ps. b) Assume we fix the clock cycle to 200 ps for a multi-cycle CPU, what is the CPI for each instruction class and the speedup over a fixed-length clock cycle? Solution: CPI for Basic ALU = 4 cycles CPI for Multiply & Divide = 6 cycles  CPI for Load = 5 cycles CPI for Store = 4 cycles CPI for Branch = 3 cycles CPI for Jump = 2 cycles Average CPI = 0.3 * 4 + 0.15 * 6 + 0.2* 5 + 0.1 * 4 + 0.15 * 3 + 0.1 * 2 = 4.15 Speedup of multi-cycle over single-cycle = (1040 * 1) / (200 * 4.15) = 1.253 Q3. (10 pts) Consider the following MIPS code sequence: a: add $t0, $s0, $s1 b: sub $t1, $s2, $t0 c: xor $t0, $s0, $s1 d: or  $t2, $t1, $t0 a) (5 pts) Identify all the RAW dependencies between pairs of instructions. Instruction b is dependent on instruction a ($t0) Instruction d is dependent on instruction b ($t1) Instruction d is dependent on instruction c ($t0) 3 b) (3 pts) Identify all the WAR dependencies between pairs of instructions Instruction c is dependent on instruction b ($t0) c) (2 pts) Identify all the WAW dependencies between pairs of instructions Instruction c is dependent on instruction a ($t0) 4 Q4. (25 pts) Use the following MIPS code fragment: I1:  ADDI $3, $0, 100  # $3 = 100 I2:  ADD  $4, $0, $0  # $4 = 0 Loop: I3:  LW  $5, 0($1)  # $5 = MEM[$1] I4:  ADD  $4, $4, $5  # $4 = $4 + $5 I5:  LW  $6, 0($2)  # $6 = MEM[$2] I6:  SUB  $4, $4, $6  # $4 = $4 – $6 I7:  ADDI $1, $1, 4  # $1 = $1 + 4 I8:  ADDI $2, $2, 4  # $2 = $2 + 4 I9:  ADDI $3, $3, -1  # $3 = $3 – 1 I10: BNE  $3, $0, Loop  # if ($3 != 0) goto Loop a) (10 pts) Show the timing of one loop iteration on the 5-stage MIPS pipeline without forwarding hardware. Complete the timing table, showing all the stall cycles. Assume that the register write is in the first half of the clock cycle and the register read is in the second half. Also assume that the branch will stall the pipeline for 1 clock cycle only. Ignore the startup cost of the pipeline. 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 1 9 20 21 22 2 3 24 25 I1 IF ID E X MEM WB I2 IF I D EX MEM WB I3 I F ID EX MEM WB I4 IF Stall Stall ID EX ME M WB I5 IF ID EX MEM WB I6 IF St al Sta ll ID EX MEM WB I7 IF ID EX MEM WB I8 IF ID EX MEM WB I9 IF ID EX MEM WB 5 I10 IF Stal l Sta ll ID EX M E WB I3 IF IF I D EX MEM WB I4 I F Stal l Sta ll ID E X MEM WB 6 b) According to the timing diagram of part (a), compute the number of clock cycles and the average CPI to execute ALL the iterations of the above loop. There are 100 iterations Each iteration requires 15 cycles = 8 cycles to start the 8 instructions in loop body + 7 stall cycles There are 2 additional cycles to start the first 2 instructions before the loop. Therefore, total cycles = 100 * 15 + 2 (can be ignored) = 1502 cycles ≈ 1500 cycles Total instruction executed = 2 + 8 * 100 = 802 instructions (counting first two) Average CPI = 1502 / 802 = 1.87 If we ignore first two instructions and the time to terminate last iteration then Average CPI = 1500/800 = 1.88 (almost same answer) 7 c) Redo part (a) to show the timing of one loop iteration with full forwarding hardware. If forwarding happens, please show how the  data is forwarded with an arrow.  1 2 3 4 5 6 7 8 9 10 1 1 12 13 14 15 16 17 18 19 20 I1 IF ID EX MEM WB I2 IF ID EX MEM WB I3 IF ID EX MEM W B I4 IF Stal l ID E X MEM WB I5 IF I D EX ME M WB I6 I F Stall ID EX M E WB I7 IF ID E X MEM WB I8 IF I D EX ME M WB I9 I F ID EX MEM WB I10 IF ID EX ME M WB I3 IF IF ID EX MEM WB I4 IF Stal l ID EX MEM WB d) Reorder the instructions of the above loop to fill the load-delay and the branch delay slots, without changing the computation. Write the code of the modified loop. ADDI $3, $0, 100  # $3 = 100 8 ADD $4, $0, $0  # $4 = 0 Loop: LW $5, 0($1)  # $5 = MEM[$1] LW $6, 0($2)  # Moved earlier to avoid load-delay ADDI $3, $3, -1  # Moved earlier ADD $4, $4, $5  # $4 = $4 + $5 ADDI $1, $1, 4  # $1 = $1 + 4 ADDI $2, $2, 4  # $2 = $2 + 4 BNE $3, $0, Loop  # if ($3 != 0) goto Loop SUB $4, $4, $6  # Fills branch delay slot e) (5 pts) Compute the number of cycles and the average CPI to execute ALL the iteration of the modified loop. What is the speedup factor? There are 100 iterations Each iteration requires 8 cycles = 8 cycles to start the 8 instructions in loop body + 0 stall cycles There are 2 additional cycles to start the first 2 instructions before the loop + 4 additional cycles to terminate the ADDI instruction in the last iteration. Therefore, total cycles = 100 * 8 + 6 (can be ignored) = 806 cycles ≈ 800 cycles Total instruction executed = 2 + 8 * 100 = 802 instructions (counting first two) Average CPI = 806 / 802 = 1.00 If we ignore first two instructions and the time to terminate last iteration then 9 Average CPI = 800/800 = 1.00 (almost same answer) Speedup Factor = CPIpart-b/CPIpart-d = 1.88/1.00 = 1.88 10 11."

#########################################
# 1. Inference for Anthropic Claude 3.7 Sonnet
#########################################
=======
query_prompt = """
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
#########################################
# 1. Inference for Anthropic Claude 4 Sonnet
#########################################

claude_inference_profile_arn_4 = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0"
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
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
=======

# #########################################
# # 2. Inference for Meta Llama3 2-90B Instruct
# #########################################

# llama_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.meta.llama3-2-90b-instruct-v1:0"

# llama_prompt = (
#     "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n"
#     f"{query_prompt}\n"
#     "<|eot_id|>\n"
#     "<|start_header_id|>assistant<|end_header_id|>"
# )
# llama_payload = {
#     "prompt": llama_prompt,
#     "max_gen_len": 512,
#     "temperature": 0.5,
# }

# response_llama = invoke_model(llama_inference_profile_arn, llama_payload)
# print("\n=== Meta Llama3 2-90B Instruct ===")
# print(response_llama)

>>>>>>> Stashed changes

#########################################
# Mistral AI Pixtrel Large
#########################################
<<<<<<< Updated upstream
mistral_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.mistral.pixtral-large-2502-v1:0"
mistral_payload = {
    "prompt": query_prompt,
    "max_tokens": 24000,
    "temperature": 0.5,
}
response_mistral = invoke_model(mistral_inference_profile_arn, mistral_payload)
print("\n=== Mistral AI Pixtrel Large ===")
print(response_mistral)
=======
# mistral_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/us.mistral.pixtral-large-2502-v1:0"
# mistral_payload = {
#     "prompt": query_prompt,
#     "max_tokens": 24000,
#     "temperature": 0.5,
# }
# response_mistral = invoke_model(mistral_inference_profile_arn, mistral_payload)
# print("\n=== Mistral AI Pixtrel Large ===")
# print(response_mistral)
>>>>>>> Stashed changes



# ########################################
# 3. Inference for Deepseek R1
# ########################################

<<<<<<< Updated upstream
deepseek_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/DeepseekProfile"

deepseek_payload = {
    "prompt": query_prompt,
    "max_tokens": 512,
    "temperature": 0.5,
}

response_deepseek = invoke_model(deepseek_inference_profile_arn, deepseek_payload)
print("\n=== Deepseek R1 ===")
print(response_deepseek)
=======
# deepseek_inference_profile_arn = "arn:aws:bedrock:us-east-2:851725383897:inference-profile/DeepseekProfile"

# deepseek_payload = {
#     "prompt": query_prompt,
#     "max_tokens": 512,
#     "temperature": 0.5,
# }

# response_deepseek = invoke_model(deepseek_inference_profile_arn, deepseek_payload)
# print("\n=== Deepseek R1 ===")
# print(response_deepseek)
>>>>>>> Stashed changes
