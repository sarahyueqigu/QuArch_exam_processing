import json
import os

folder = "auto checked"

# Previously we hand-checked some exams before running them through the autochecker. This program is designed to combine
# both the autochecker "correctly_parsed" field and the human-iputted "correctly-parsed" field into one JSON file
for file in os.listdir(folder):
    if file.endswith(".json"):

        print("PROCESSING:", file)

        autochecked_path = os.path.join(folder, file)
        
        with open(autochecked_path, 'r') as f:
            llm_checked = json.load(f)
        
        for llm in llm_checked:
            print("SUB-PROCESS:", llm["question_id"])
            llm["passed_human_verification"] = None
            # print(hum)

        with open(autochecked_path, 'w') as f:
            json.dump(llm_checked, f, indent=4)



        
