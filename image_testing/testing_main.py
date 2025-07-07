import sys, pymupdf
import os
import testing_yolo
import testing_opencv
import test_fitz_pymupdf
import testing_pdfplumber
import testing_scikit
import image_extraction_singlepdf


# for filename in os.listdir("data"):
#     if filename.lower().endswith(".pdf"): 
#         doc = pymupdf.open(os.path.join("data", filename))  # open document

#         pdf_output_dir = os.path.join("manual_figure_extraction", "pdf_to_image", filename[:-4])
#         os.makedirs(pdf_output_dir, exist_ok = True)

#         for page in doc:  # iterate through the pages
#             filename = "page-%i.png" % page.number
#             pix = page.get_pixmap()  # render page to an image
#             new_path = os.path.join(pdf_output_dir, filename)
#             pix.save(new_path)  # store image as a PNG

# input_dir = "manual_figure_extraction/pdf_to_image"

# # # For the libraries that scrape the images from the pdf's directly
# # test_fitz_pymupdf.execute()
# # testing_pdfplumber.execute()

# # For the libraries that require converting the pdf into images:
# for exam in os.listdir(input_dir):
#     for page in os.listdir(os.path.join(input_dir, exam)):
#         input_path = os.path.join(input_dir, exam, page)
#         # testing_yolo.execute(input_path, exam, page)
#         # testing_opencv.execute(input_path, exam, page)
#         testing_scikit.execute(input_path, exam, page)


parent_dir = "manual_figure_extraction/llamaparse"
os.makedirs(parent_dir, exist_ok=True)
# Testing Llamaparse
for filename in os.listdir("data"):
    if filename.lower().endswith(".pdf"): 
        file_path = os.path.join("data", filename)

        output_dir = os.path.join(parent_dir, filename[:-4])
        os.makedirs(output_dir, exist_ok=True)

        image_extraction_singlepdf.process(filename, file_path, output_dir)