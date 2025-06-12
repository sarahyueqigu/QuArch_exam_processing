import table_extraction
from mistralai import Mistral
import json
from pathlib import Path ## makes file directory paths objects, good for readability 
import re
import argparse
import os

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
input_dir  = Path("/Users/aliceguo/Documents/QuArch_exam_processing/quarch_alice_main/small_sample_exams") 
##local path to folder of quarch exams in markdown, replace with your own path
output_js  = Path("parsed_qa.json")

prompt_template = """
    You are a language model assisting with the digitization of academic exam content. The input is an exam which has been parsed into Markdown text. The exam contains one or more problems from a Computer Architecture assessment. A problem may include any combination of the following:
A context paragraph, or just a short statement (e.g., “Convert the number 42 to binary”)
One or more sub-questions, or be a single standalone question
Context for sub-questions separate from the sub-question and separate from the original problem context
Multiple questions within a subquestion
Point value associations for the problem or subproblems, including extra credit points
Solutions, either typed or handwritten
Tables, diagrams, circuit schematics, or block diagrams
Parse the following markdown problem file and classify its components into JSON with this format:
{
  "problem": <problem number or identifier>,
  "problem_context": <introductory text, if any>,
  "problem_figures": [<list of image filenames referenced in the context>],
  "parts": [
    {
      "part": <subproblem letter or number>,
      "question": [
        {
          "subproblem_context": <subproblem context, if any>,
          "subproblem_question": <full text of the subproblem question>,
          "subproblem_figures": [<images referenced in the question>]  
        }
      ],
      "answer": [
        {
          "solution": <solution text exactly as appears>,
          "solution_figures": [<images in the solution>]
        }
      ]
    }
    # ... repeat for each part
  ]
}

Here is the markdown content:
```
{markdown_content}
```

And here are the image filenames available:
{image_list}

Respond with valid JSON only.  
"""


def list_markdown_files(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path)
            if f.lower().endswith('.md')]

def extract_image_refs(markdown_text):
    # Regex for markdown image syntax ![alt](path)
    return re.findall(r"!\[[^\]]*\]\(([^)]+)\)", markdown_text)

def call_mistral(prompt):
    # headers = {
    #     "Authorization": f"Bearer {api_key}",
    #     "Content-Type": "application/json"
    # }
    # payload = {
    #     "model": "mistral-large",  # adjust model name as needed
    #     "prompt": prompt,
    #     "max_tokens": 2000
    # }
    chatResponse = client.chat.complete(
        model="mistral-large-latest",
        messages=[{"role": "user", "content": prompt}],
        response_format="json_object",   # correct snake_case
        max_tokens=2000,
    )

    return getattr(chatResponse, "completion", chatResponse.choices[0].message.content)


def parse_and_classify(md_file, images_dir):
    content = Path(md_file).read_text(encoding="utf-8")
    refs = extract_image_refs(content)
    image_list = [os.path.basename(r) for r in refs]
    prompt = prompt_template.format(
        markdown_content=content,
        image_list=json.dumps(image_list)
    )

    raw = call_mistral(prompt)
    print(f"\n─── RAW MISTRAL OUTPUT for {md_file} ───\n{raw}\n")

    # 1) If we already have a dict, return it
    if isinstance(raw, dict):
        return raw

    # 2) Strip fences and extra text
    clean = re.sub(r"```(?:json|text)?\s*", "", raw)
    m = re.search(r"\{.*\}", clean, flags=re.DOTALL)
    if not m:
        print(f"❗ No JSON found in Mistral reply:\n{repr(raw)}")
        raise ValueError("No JSON object in output")
    json_str = m.group(0).strip()

    # 3) Parse
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print("❗ Failed to parse JSON:\n", json_str)
        print("→ JSONDecodeError:", e)
        raise


def natural_key(problem_id):
    # Extract first integer for sorting
    nums = re.findall(r"\d+", str(problem_id))
    return int(nums[0]) if nums else str(problem_id)

def main(md_folder, img_folder, output_file):
    results = []
    for md_path in list_markdown_files(md_folder):
        try:
            res = parse_and_classify(md_path, img_folder)
            results.append(res)
        except Exception as e:
            print(f"Error processing {md_path}: {e}")
    # Sort by problem identifier
    results.sort(key=lambda x: natural_key(x.get('problem', '')))
    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(str(results))
    print(f"Classified {len(results)} problems. Output saved to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Classify markdown problems using Mistral AI")
    parser.add_argument('md_folder', help="Path to folder with markdown files")
    parser.add_argument('img_folder', help="Path to folder with images")
    parser.add_argument('-o', '--output', default='classified_problems.json',
                        help="Output JSON filename")
    args = parser.parse_args()
    main(args.md_folder, args.img_folder, args.output)
