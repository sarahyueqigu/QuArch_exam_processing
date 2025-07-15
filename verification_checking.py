import json
import os
import csv

fieldnames = ["exam", "testing_version", "total", "concurred_trues", "concurred_falses", "false_trues", "true_falses",
              "verified_trues", "api_trues", "total_questions_no_images", "concurred_trues_no_images", 
              "concurred_falses_no_images", "api_accuracy", "llm_accuracy", "llm_accuracy_no_images"]

# false_trues is where the api thinks it's true when it's actually false
# true_falses is where the api thinks it's false when it's actually true 

# input_dir is from verification_tests/exam_name
def process(input_dir, exam):
    
    # Process each API verification test
    for api_test in os.listdir(input_dir):

        # Open the results from the verification pipeline

        row = {
            "exam": exam,
            "testing_version": "problem by problem (verification pipeline version 2)",
            "total": 0.0,
            "concurred_trues": 0.0,
            "concurred_falses": 0.0, 
            "false_trues": 0.0,
            "true_falses": 0.0,
            "verified_trues": 0.0, 
            "api_trues": 0.0, 
            "total_questions_no_images": 0.0,
            "concurred_trues_no_images": 0.0,
            "concurred_falses_no_images": 0.0,
            "llm_accuracy": 0.0,
            "llm_accuracy_no_images": 0.0
        }
        
        json_path = os.path.join(input_dir, api_test)
        with open(json_path, "r") as file:
            verification_test_json = json.load(file)
        
        # Open the hand_verifiedly checked results
        checked_path = os.path.join("checked", "[CHECKED]" + exam + ".json")
        with open(checked_path, "r") as file:
            hand_verifiedly_checked_json = json.load(file)
        
        for llm_verified, hand_verified in zip(verification_test_json, hand_verifiedly_checked_json):
            print("Processing problem:", llm_verified["question_id"])
            row["total"] += 1
            # print("llm_verified[correctly_parsed]: ", llm_verified["correctly_parsed"])
            # print("hand_verified[correctly_parsed]: ", hand_verified["correctly_parsed"])

            # Check if the problem has images
            has_images = True
            if not hand_verified["context_figures"] and not hand_verified["solution_figures"]:
                has_images = False
                row["total_questions_no_images"] += 1

            if llm_verified["correctly_parsed"] == True and hand_verified["correctly_parsed"] == True:
                row["concurred_trues"] += 1
                if not has_images:
                    row["concurred_trues_no_images"] += 1
            elif llm_verified["correctly_parsed"] == False and hand_verified["correctly_parsed"] == False:
                row["concurred_falses"] += 1
                if not has_images:
                    row["concurred_falses_no_images"] += 1
            elif llm_verified["correctly_parsed"] == True and hand_verified["correctly_parsed"] == False:
                row["true_falses"] += 1
            else:
                row["false_trues"] += 1

            if llm_verified["correctly_parsed"] == True:
                row["api_trues"] += 1
            if hand_verified["correctly_parsed"] == True:
                row["verified_trues"] += 1
        
        row["llm_accuracy"] = (row["concurred_trues"] + row["concurred_falses"]) / row["total"]
        row["llm_accuracy_no_images"] = (row["concurred_falses_no_images"] + row["concurred_trues_no_images"]) / row["total"]
        print(row)

        # Open the CSV in append mode
        with open('verification_checking.csv', 'a', newline='') as file:
            # Define fieldnames matching the CSV header
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the row
            writer.writerow(row)



if __name__ == "__main__":
    exam = "740_f13_midterm2_solutions"
    # parent_dir = os.path.join("llm_verification_v2", exam)
    process("llm_verification_v2", exam)

    # with open("verification_checking.csv", "w", newline="") as file:
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)

    # for exam in os.listdir(parent_dir):
        
    #     path = os.path.join(parent_dir, exam)
    #     print(path)
    #     process(path, exam)c