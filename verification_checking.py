import json
import os
import csv

fieldnames = ["exam", "testing_version", "total", "concurred_trues", "concurred_falses", "false_trues", 
              "true_falses", "verified_trues", "llm_trues", "total_questions_no_images", 
              "concurred_trues_no_images", "concurred_falses_no_images", "false_trues_no_images", 
              "true_falses_no_images", "llm_accuracy", "llm_accuracy_no_images", "false_trues_questions"]

# false_trues is where the api thinks it's true when it's actually false
# true_falses is where the api thinks it's false when it's actually true 

def process_single(input_dir):
    exam = os.path.basename(input_dir)
     # Open the results from the verification pipeline

    row = {
        "exam": exam,
        "testing_version": "grace_verifying",
        "total": 0.0,
        "concurred_trues": 0.0,
        "concurred_falses": 0.0, 
        "false_trues": 0.0,
        "true_falses": 0.0,
        "verified_trues": 0.0, 
        "llm_trues": 0.0, 
        "total_questions_no_images": 0.0,
        "concurred_trues_no_images": 0.0,
        "concurred_falses_no_images": 0.0,
        "false_trues_no_images": 0.0,
        "true_falses_no_images": 0.0,
        "llm_accuracy": 0.0,
        "llm_accuracy_no_images": 0.0,
        "false_trues_questions": []
    }
    
    with open(input_dir, "r") as file:
        json_file = json.load(file)
    
    for problem in json_file:
        print("Processing problem:", problem["question_id"])
        row["total"] += 1
        # print("llm_verified[correctly_parsed]: ", llm_verified["correctly_parsed"])
        # print("hand_verified[correctly_parsed]: ", hand_verified["correctly_parsed"])

        # Check if the problem has images
        has_images = True
        if not problem["context_figures"] and not problem["solution_figures"]:
            has_images = False
            row["total_questions_no_images"] += 1

        if problem["passed_llm_verification"] == True and problem["passed_human_verification"] == True:
            row["concurred_trues"] += 1
            if not has_images:
                row["concurred_trues_no_images"] += 1
        elif problem["passed_llm_verification"] == False and problem["passed_human_verification"] == False:
            row["concurred_falses"] += 1
            if not has_images:
                row["concurred_falses_no_images"] += 1

        elif problem["passed_llm_verification"] == True and problem["passed_human_verification"] == False:
            row["true_falses"] += 1
            if not has_images:
                row["true_falses_no_images"] += 1
        else:
            row["false_trues"] += 1
            row["false_trues_questions"].append(problem["question_id"])
            if not has_images:
                row["false_trues_no_images"] += 1

        if problem["passed_llm_verification"] == True:
            row["llm_trues"] += 1
        if problem["passed_human_verification"] == True:
            row["verified_trues"] += 1
    
    row["llm_accuracy"] = (row["concurred_trues"] + row["concurred_falses"]) / row["total"]
    row["llm_accuracy_no_images"] = (row["concurred_falses_no_images"] + row["concurred_trues_no_images"]) / row["total_questions_no_images"]
    print(row)

    # Open the CSV in append mode
    with open('verification_checking.csv', 'a', newline='') as file:
        # Define fieldnames matching the CSV header
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the row
        writer.writerow(row)

# input_dir is from verification_tests/exam_name
# Process multiple apis (version 1)
def process_v1(input_dir, exam):
    
    # Process each API verification test
    for verification_output in os.listdir(input_dir):
        process_single(input_dir, exam, verification_output)

       



if __name__ == "__main__":
    exam = "exam_solutions_ss2012"
    # parent_dir = os.path.join("llm_verification_v2", exam)
    # process_v1("llm_verification_v2", exam)

    file = "[AUTO_CHECKED]exam_solutions_ss2012.json"
    input_dir = "final"

    for file in os.listdir(input_dir):
        process_single(os.path.join(input_dir, file))

    # with open("verification_checking.csv", "w", newline="") as file:
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)

    # for exam in os.listdir(parent_dir):
        
    #     path = os.path.join(parent_dir, exam)
    #     print(path)
    #     process(path, exam)c