import json
import os
import csv

fieldnames = ["exam", "api", "total", "concurred_trues", "concurred_falses", "checked_trues", 
              "api_trues", "api_accuracy"]

# input_dir is from verification_tests/exam_name
def process(input_dir, exam):
    
    # Process each API verification test
    for api_test in os.listdir(input_dir):

        # Open the results from the verification pipeline

        row = {
            "exam": exam,
            "api": api_test[:-5],
            "total": 0.0,
            "concurred_trues": 0.0,
            "concurred_falses": 0.0, 
            "checked_trues": 0.0, 
            "api_trues": 0.0, 
            "api_accuracy": 0.0
        }
        
        json_path = os.path.join(input_dir, api_test)
        with open(json_path, "r") as file:
            verification_test_json = json.load(file)
        
        # Open the manuall ychecked results
        checked_path = os.path.join("checked", "[CHECKED]" + exam + ".json")
        with open(checked_path, "r") as file:
            manually_checked_json = json.load(file)
        
        for verify, manual in zip(verification_test_json, manually_checked_json):
            row["total"] += 1
            print("verify[correctly_parsed]: ", verify["correctly_parsed"])
            print("manual[correctly_parsed]: ", manual["correctly_parsed"])

            if verify["correctly_parsed"] == True and manual["correctly_parsed"] == True:
                row["concurred_trues"] += 1
            elif verify["correctly_parsed"] == False and manual["correctly_parsed"] == False:
                row["concurred_falses"] += 1

            if verify["correctly_parsed"] == True:
                row["api_trues"] += 1
            if manual["correctly_parsed"] == True:
                row["checked_trues"] += 1
        
        row["api_accuracy"] = (row["concurred_trues"] + row["concurred_falses"]) / row["total"]

        # Open the CSV in append mode
        with open('verification_checking.csv', 'a', newline='') as file:
            # Define fieldnames matching the CSV header
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the row
            writer.writerow(row)


if __name__ == "__main__":
    parent_dir = "verification_tests"
    exam = 
    process(parent_dir, exam)

    # for exam in os.listdir(parent_dir):
        
    #     path = os.path.join(parent_dir, exam)
    #     print(path)
    #     process(path, exam)