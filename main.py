import os
import text_extraction
import image_extraction_singlepdf
import image_identifing
import problem_extraction
import problem_image_extraction
#6/30 SUPPORTED list of supported file types added so that the script doesnt try to run on files that aren't pdf files
#the added lines i marked with a #6/30 comment

SUPPORTED = ('.pdf',)   #supported file types #6/30

if __name__ == "__main__":
    parent_folder = "10_onur_exams" #7/2 running the pipeline on the 10_onur_exams folders
    print(os.listdir(parent_folder))
    input_dir = parent_folder

    # Parse through each file in the subfolder
    for filename in os.listdir(input_dir):
        #if filename == "sp18-final-sol.pdf":
        path = os.path.join(input_dir, filename)
        # skip anything that isn’t a file or doesn’t end with .pdf
        if not os.path.isfile(path) or not filename.lower().endswith(SUPPORTED): #6/30
            continue #6/30
        file_dir = input_dir + "/" + filename

        data = problem_image_extraction.process(file_dir, "10_onur_exams_output")
        matches = image_identifing.process(file_dir, data, "10_onur_exams_output")
        text_extraction.process(file_dir, "output","10_onur_exams_output", matches)
            
        
        
            
            
            
