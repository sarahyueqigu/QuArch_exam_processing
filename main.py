import os
import text_extraction
import image_extraction_singlepdf
import subprocess
import image_identifing
import problem_page_extraction

if __name__ == "__main__":
    parent_folder = "/Users/aliceguo/Documents/QuArch_exam_processing/OnurETHZ_exams_test2"
    print(os.listdir(parent_folder))
    input_dir = parent_folder

    # Parse through each file in the subfolder
    for filename in os.listdir(input_dir): # TODO: may cause some delays when .json files are added
        # Build path             
        file_dir = input_dir + "/" + filename

        data = problem_page_extraction.process(file_dir)
        matches = image_identifing.process(file_dir, data)
        text_extraction.process(file_dir, matches)
        
    
    
        
        
        
