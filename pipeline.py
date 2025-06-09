import table_extraction
from mistralai import Mistral
import json
from pathlib import Path ## makes file directory paths objects, good for readability 
import markdown
from bs4 import BeautifulSoup ##for parsing html, xml

#### packages
# pip install pdfplumber
# pip install mistralai
# pip install pymupdf
# pip install os
# pip install pymupdf4llm
# pip install pydantic

api_key = "IffIovWq8tUyBc2oinkenZXp2MeqnALs"
model = "mistral-large-latest"

client = Mistral(api_key=api_key)


#____________________________________________________________
# pdf as markdown text parsing, taking in the extracted images, 
# returning a json file with problem(text), context(text and image file path), solution (text)
#____________________________________________________________
input_dir  = Path("/Users/aliceguo/Documents/QuArch_exam_processing/quarch_alice_main/out_folder") 
##local path to folder of quarch exams in markdown, replace with your own path
output_js  = Path("parsed_qa.json")

parsing_prompt = """
    You are a language model assisting with the digitization of academic exam content. The input is an exam which has been parsed into Markdown text. The exam contains one or more problems from a Computer Architecture assessment. A problem may include any combination of the following:
A context paragraph, or just a short statement (e.g., “Convert the number 42 to binary”)
One or more sub-questions, or be a single standalone question
Context for sub-questions separate from the sub-question and separate from the original problem context
Multiple questions within a subquestion
Point value associations for the problem or subproblems, including extra credit points
Solutions, either typed or handwritten
Tables, diagrams, circuit schematics, or block diagrams
Your task is to identify and separate each exam problem into the listed components, including context, sub-questions, and solutions. If you encounter any images and tables, do not attempt to copy them. Instead, replace them with [IMAGE] or [TABLE] accordingly. Ignore any point values for any problem, question, or sub-question. Format your response using the template below. If the particular exam question lacks any of the listed components, do not include them.

## Problem Number
Problem Context: <Fill in here> 

Sub-question 1. 
Sub-question context: <Fill in here> 
Figure context: <Fill in here>
Question: <Fill in here> 
Solution: <Fill in here> 

Sub-question 2. 
Sub-question context: <Fill in here> 
Figure context: <Fill in here>
Question: <Fill in here> 
Solution: <Fill in here> 
…
"""


