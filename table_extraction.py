import pdfplumber
import fitz  # PyMuPDF
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
import layoutparser as lp

# # Suppress the warnings WARNING:pdfminer.pdfpage:CropBox missing from /Page, defaulting to MediaBox
# import logging
# logging.getLogger("pdfminer").setLevel(logging.ERROR)


# # Extract tables as images
# # THIS EXTRACTS TEH ENTIRE PAGE
# with pdfplumber.open(pdf_path) as pdf:
#     for i, page in enumerate(pdf.pages):
#         tables = page.extract_tables()
#         if tables:
#             # Save page as image
#             im = page.to_image(resolution=150)
#             im_path = f"page_{i+1}_with_table.png"
#             im.save(im_path)
#             print(f"Saved {im_path}")

    
import os

pdf_path = "../data/CDA 4205 Computer Architecture Exam 2 Practice Solution-2.pdf"
pdf_layout = lp.load_pdf(pdf_path)
pdf_layout[0] # the layout for page 0
pdf_layout, pdf_images = lp.load_pdf(pdf_path, load_images=True)
lp.draw_box(pdf_images[0], pdf_layout[0])


# # Extract the tables (DATA SCRAPING)
# with pdfplumber.open(pdf_path) as pdf:
#     for page in pdf.pages:
#         tables = page.extract_tables()
#         for table in tables:
#             for row in table:
#                 print(row)


# doc = fitz.open("../data/CDA 4205 Computer Architecture Exam 2 Practice Solution-2.pdf")
# for page_number in range(len(doc)):
#     images = doc[page_number].get_images(full=True)
#     for img_index, img in enumerate(images):
#         xref = img[0]
#         pix = fitz.Pixmap(doc, xref)
#         if pix.n < 5:  # this is GRAY or RGB
#             pix.save(f"image_{page_number+1}_{img_index+1}.png")
#         pix = None

