import os
import text_extraction
import image_extraction
import subprocess

if __name__ == "__main__":
    # subprocess.run(["python3", "problem_page_extraction.py"])

    parent_folder = "extracted_problems"
    print(os.listdir(parent_folder))
    os.makedirs("extracted_problems", exist_ok=True)

    for folder in os.listdir(parent_folder):
        input_dir =  parent_folder + "/" + folder
        print(input_dir)

        # Extract all the images in each file
        # image_extraction.process(input_dir)


        # i know parsing through all the files in the folder at once and then parsing through each file individually is
        # weird but idk how to fix it in image_exctraction

        # Create the JSON for each problem
        for filename in os.listdir(input_dir):
          
          print(filename)
          
          # Only process PDFs
          if filename.lower().endswith(".pdf"):
             
             # Output path
             output_dir = "extracted_problems/" + filename[:-4]

             text_extraction.process(filename, input_dir + "/" + filename, output_dir)
            #  image_extraction.process(filename, input_dir)
        
        # # Create the image (use scandir for more speed)
        # with os.scandir(folder) as it:
        #     for entry in it:
        #         if entry.is_dir():
                    
        
        
        