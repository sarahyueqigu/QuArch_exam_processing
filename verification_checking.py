import json
import os
import csv


# input_dir is from verification_tests/exam_name
def process(input_dir, exam):
    
    # Process each API verification test
    for api_test in input_dir:
        json_path = os.path.join(input_dir, api_test)
        with open(json_path, "r") as file:
            verification_test = json.load(file)
        
        for problem in verification_test:
    

        
        # Append to the CSV file
        with open("output.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_data)


if __name__ == "__main__":
    # Need to declare this in main.py potentially?
    header = ["exam", "api", "concurred_trues", "concurred_falses", "checked_trues", 
              "api_trues", "api_accuracy"]
    
    with open("output.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(header)