import json
import os

folder = "checked"

# Previously we hand-checked some exams before running them through the autochecker. This program is designed to combine
# both the autochecker "correctly_parsed" field and the human-iputted "correctly-parsed" field into one JSON file
for file in os.listdir(folder):
    if file.endswith(".json"):

        print("PROCESSING:", file)

        exam = file[9:]
        checked_path = os.path.join(folder, file)

        with open(checked_path, 'r') as f:
            human_checked = json.load(f)
        
        autochecked_path = os.path.join("auto checked", "[AUTO_CHECKED]" + exam)
        with open(autochecked_path, 'r') as f:
            llm_checked = json.load(f)
        
        for llm, hum in zip(llm_checked, human_checked):
            print("SUB-PROCESS:", llm["question_id"])
            hum["passed_human_verification"] = hum.pop("correctly_parsed")
            hum["passed_llm_verification"] = llm["correctly_parsed"]
            # print(hum)

        
        out_dir = "final"
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "[FINAL]" + exam)

        with open(out_path, 'w') as f:
            json.dump(human_checked, f, indent=4)



        
