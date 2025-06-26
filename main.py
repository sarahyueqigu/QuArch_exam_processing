import os
import text_extraction
import image_extraction_singlepdf
import subprocess
import image_identifing

if __name__ == "__main__":
    # subprocess.run(["python3", "problem_page_extraction.py"])

    parent_folder = "OnurETHZ_exams_parsed1"
    print(os.listdir(parent_folder))
    # os.makedirs("OnurETHZ_exams", exist_ok=True)
    input_dir = parent_folder

    # for folder in os.listdir(parent_folder):
    #     input_dir =  parent_folder + "/" + folder
    #     print("input_dir:", input_dir)

        # for problem_folder in os.listdir(input_dir):

        #     input_dir = parent_folder + "/" + folder + "/" + problem_folder
        #     # Extract all the images in each file at once
        #     # image_extraction.process(input_dir)

        # # Ensure this is not hte .DS_Store file
        # if folder != ".DS_Store":

    # Parse through each file in the subfolder
    for filename in os.listdir(input_dir): # TODO: may cause some delays when .json files are added
        # Only process PDFs
        if filename.lower().endswith(".pdf"):             
            # Output path
            output_dir = input_dir + "/" + filename[:-4]
            os.makedirs(output_dir, exist_ok=True)

            print("output_dir: ", output_dir)

            text_extraction.process(filename, input_dir + "/" + filename, input_dir)
            image_extraction_singlepdf.process(filename, input_dir + "/" + filename, input_dir + "/" + filename[:-4])
            image_identifing.process(filename, input_dir + "/" + filename[:-4])
        
    
        
        # # Create the image (use scandir for more speed)
        # with os.scandir(folder) as it:
        #     for entry in it:
        #         if entry.is_dir():
                    
        
        
        