import os
import asyncio
import config
import text_extraction
import problem_image_extraction
import json

if __name__ == "__main__":
    parent_folder = "OnurETHZ_exams"
    print(os.listdir(parent_folder))
    input_dir = parent_folder


    # Parse through each file in the subfolder
    for filename in os.listdir(input_dir): # TODO: may cause some delays when .json files are added
        # Only process PDFs
        if filename == "740_f13_midterm2_solutions.pdf":
        # if filename.lower().endswith(".pdf"):   
            # Build path             
            file_dir = input_dir + "/" + filename
            data = problem_image_extraction.process(file_dir, "extracted_problems", arn)

            # Loop through each arn
            for api in dir(config):

                # Skip built-in attributes (those starting with __)
                if not api.startswith("__"):
                    print(api)
                    arn = getattr(config, api)

                    print("went here")
                    text_extraction.process(file_dir, data, arn, api)

            
            
            
c