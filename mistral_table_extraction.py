import pdfplumber
import fitz  # PyMuPDF
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



# # Suppress the warnings WARNING:pdfminer.pdfpage:CropBox missing from /Page, defaulting to MediaBox
# import logging
# logging.getLogger("pdfminer").setLevel(logging.ERROR)

# Extract the tables
with pdfplumber.open("../data/CDA 4205 Computer Architecture Exam 2 Practice Solution-2.pdf") as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                print(row)


# doc = fitz.open("../data/CDA 4205 Computer Architecture Exam 2 Practice Solution-2.pdf")
# for page_number in range(len(doc)):
#     images = doc[page_number].get_images(full=True)
#     for img_index, img in enumerate(images):
#         xref = img[0]
#         pix = fitz.Pixmap(doc, xref)
#         if pix.n < 5:  # this is GRAY or RGB
#             pix.save(f"image_{page_number+1}_{img_index+1}.png")
#         pix = None