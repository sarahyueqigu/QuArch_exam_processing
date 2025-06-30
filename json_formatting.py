#!/usr/bin/env python3
"""
Convert a folder of “old” JSON exam/problem files into a flat list
of {"exam_name", "question_number", "question", "context", "context_figures",
 "answer", "answer_figures"} records and write to one output file.
Handles double‐encoded JSON and single‐object files.
"""
#dont work lol

import json
import argparse
from pathlib import Path
import sys

def load_json_maybe_string(path: Path):
    text = path.read_text(encoding="utf-8")
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"✖ Failed to parse {path}: {e}", file=sys.stderr)
        return None

    # Unwrap double‐encoded JSON strings
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            pass

    # If we get a single dict at top level, treat it as a list of one problem
    if isinstance(data, dict):
        data = [data]
    elif not isinstance(data, list):
        print(f"✖ Expected a list or dict in {path}, got {type(data).__name__}", file=sys.stderr)
        return None

    return data

def convert_json_folder(input_folder: Path, output_path: Path):
    output = []

    for json_file in sorted(input_folder.glob("*.json")):
        print(f"DEBUG: loading {json_file}", file=sys.stderr)
        exam_name = json_file.stem
        problems = load_json_maybe_string(json_file)
        if problems is None:
            print(f"DEBUG:   → skipped (couldn’t parse or unsupported type)", file=sys.stderr)
            continue
        print(f"DEBUG:   → found {len(problems)} top-level items", file=sys.stderr)
        for problem in problems:
            print(f"DEBUG: problem keys for {json_file.name} → {list(problem.keys())}")
            if not isinstance(problem, dict):
                print(f"⚠ Skipping non-dict entry in {json_file}: {problem!r}", file=sys.stderr)
                continue

            prob_num  = problem.get("problem", "")
            prob_ctx  = problem.get("problem_context", "").strip()
            prob_figs = problem.get("problem_figures", [])

            for part in problem.get("parts", []):
                parts = problem.get("parts")
                print(f"DEBUG:   parts field is {type(parts).__name__}: {parts}", file=sys.stderr)
                for part in parts or []:
                    # print the actual keys at the part level
                    print(f"DEBUG: part keys → {list(part.keys())}", file=sys.stderr)

                part_label = str(part.get("part", "")).strip()
                questions = part.get("question", [])
                answers   = part.get("answer", [])
                print(f"DEBUG:   question list type={type(questions).__name__}, answer list type={type(answers).__name__}", file=sys.stderr)

                for q_item, a_item in zip(questions, answers):
                    print(f"DEBUG:     q_item keys → {list(q_item.keys())}", file=sys.stderr)
                    sprint(f"DEBUG:     a_item keys → {list(a_item.keys())}", file=sys.stderr)
                    sub_ctx   = q_item.get("subproblem_context", "").strip()
                    sub_figs  = q_item.get("subproblem_figures", [])
                    context       = sub_ctx or prob_ctx
                    context_figures = sub_figs if sub_ctx else prob_figs

                    rec = {
                        "exam_name": exam_name,
                        "question_number": f"{prob_num}{part_label}",
                        "question": q_item.get("subproblem_question", "").strip(),
                        "context": context,
                        "context_figures": context_figures,
                        "answer": a_item.get("solution", "").strip(),
                        "answer_figures": a_item.get("solution_figures", []),
                    }
                    output.append(rec)

    # with output_path.open("w", encoding="utf-8") as f:
    #     json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"DEBUG: total records to write = {len(output)}", file=sys.stderr)
    if not output:
        print("WARNING: no records found—check that your JSON files actually contain the expected fields!", file=sys.stderr)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

def main():
    p = argparse.ArgumentParser(
        description="Transform old-format exam JSONs to flat new-format JSON."
    )
    p.add_argument("input_folder", type=Path,
                   help="Directory containing old-format *.json files")
    p.add_argument("output_file",   type=Path,
                   help="Path to write the combined new-format JSON")
    args = p.parse_args()

    if not args.input_folder.is_dir():
        print(f"✖ {args.input_folder} is not a directory", file=sys.stderr)
        sys.exit(1)

    convert_json_folder(args.input_folder, args.output_file)
    print(f"✔ Converted files in {args.input_folder!r} → {args.output_file!r}")

if __name__ == "__main__":
    main()
