import os
import text_extraction
import image_extraction_singlepdf
import subprocess
import image_identifing
import problem_page_extraction

if __name__ == "__main__":
    parent_folder = "in"
    print(os.listdir(parent_folder))
    input_dir = parent_folder

    # Parse through each file in the subfolder
    for filename in os.listdir(input_dir): # TODO: may cause some delays when .json files are added
        # Only process PDFs
        if filename.lower().endswith(".pdf"):
            # Build path             
            file_dir = input_dir + "/" + filename

            data = problem_page_extraction.process(file_dir)
            matches = image_identifing.process(file_dir, data)
            text_extraction.process(file_dir, "output", matches)
        
    
    
        
        
        
