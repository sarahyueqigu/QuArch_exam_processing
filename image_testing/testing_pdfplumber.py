import pdfplumber
import math
import pymupdf
from PIL import Image
import os
import fitz
import sys

def detect_all_tables(pdf_path, stream_mode=False):
    """
    Detects all tables in the given PDF and returns a list of dicts,
    one per table, with page number, bounding box, and optionally cell data.
    
    Args:
        pdf_path (str): Path to the PDF file.
        stream_mode (bool): If True, use a text‐based ("stream") detection strategy
                            rather than relying on ruling lines ("lattice"). Defaults to False.
    
    Returns:
        List[dict]: Each dict has:
            - 'page_num' (int): 0‐based page index
            - 'bbox'     (tuple): (x0, top, x1, bottom) in PDF points
            - 'cells'    (List[dict]): Optional: each cell’s bbox and text
    """
    all_tables = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):

            if stream_mode:
                # If your tables have no borders, use text‐based detection:
                settings = {
                    "vertical_strategy":   "text",
                    "horizontal_strategy": "text",
                }
                tables = page.find_tables(table_settings=settings)
            else:
                # Default: detect by looking for ruling lines / borders
                tables = page.find_tables()
            
            for tbl_idx, table in enumerate(tables):
                x0, top, x1, bottom = table.bbox
                width = x1 - x0
                height = top - bottom
                
                # If you just want bbox info:
                table_info = {
                    "page_num": page_num,
                    "table_index_on_page": tbl_idx,
                    "bbox": (x0, top, x1, bottom),
                    "width": width,
                    "height": height,
                    # If you want cell‐by‐cell details:
                    "cells": []
                }
                
                all_tables.append(table_info)
    
    return all_tables


def process_pdfplumber(file_dir, filename):
    print("MANUAL FIGURE EXTRACTION:", file_dir)
    # Now `filepath` is the path to one PDF file

    output_dir = "manual_figure_extraction/pdf_plumber1/" + filename

    # 1. Create the target directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open both libraries’ handles
    file_pymupdf = pymupdf.open(file_dir)
    file_plumber = pdfplumber.open(file_dir)
    page_count = len(file_plumber.pages)

    # 2. Extract full‐page images via PyMuPDF and save into output_dir
    for page_number in range(page_count):
        images = file_pymupdf[page_number].get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            pix = pymupdf.Pixmap(file_pymupdf, xref)
            if pix.n < 5:  # GRAY or RGB
                filename = f"page_{page_number+1}_img_{img_index+1}.png"
                save_path = os.path.join(output_dir, filename)
                pix.save(save_path)
            pix = None  # free the Pixmap

    # 3. Detect tables (via pdfplumber), crop them, and save each cropped region into output_dir
    tables = detect_all_tables(file_dir, stream_mode=False)
    print(f"Found {len(tables)} tables (lattice).")
    counter = 0
    for t in tables:
        p = t["page_num"]
        bbox = t["bbox"]
        x1, top, x2, bottom = bbox
        # Convert PDF‐points box → integer pixel box at 150 DPI
        scale = 150 / 72
        left   = int(math.floor(x1) * scale)
        top_px  = int(math.floor(top) * scale)
        right  = int(math.ceil(x2) * scale)
        bottom_px = int(math.ceil(bottom) * scale)

        page = file_plumber.pages[p]
        pil_image = page.to_image(resolution=150).original 

        cropped = pil_image.crop((left, top_px, right, bottom_px))
        filename = f"table_crop_{counter:03d}.png"
        save_path = os.path.join(output_dir, filename)
        cropped.save(save_path)

        print(f"Saved {save_path}")
        counter += 1

    file_plumber.close()
    file_pymupdf.close()


def process_fitz(file_dir, filename):
    doc = fitz.open(file_dir)

    output_folder = "manual_figure_extraction/fitz/" + filename  # your desired folder name
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for page in doc:
        pix = page.get_pixmap()  # render the page as an image
        output_path = os.path.join(output_folder, f"page-{page.number + 1}.png")
        pix.save(output_path)  # save to the specified folder

        # for img_index, img in enumerate(doc.get_page_images(page_index)):
        #     xref = img[0]
        #     base_image = doc.extract_image(xref)
        #     image_bytes = base_image["image"]
        #     image_ext = base_image["ext"]
            
        #     # Modify your file writing line like this:
        #     filename = f"image_page{page_index+1}_{img_index}.{image_ext}"
        #     filepath = os.path.join(output_folder, filename)
        #     with open(filepath, "wb") as f:
        #         f.write(image_bytes)



def execute():
    input_dir = "data"

    for filename in os.listdir(input_dir):
        # Build full path
        file_dir = os.path.join(input_dir, filename)
        
        # Only process PDFs
        if file_dir.lower().endswith(".pdf"):
            process_pdfplumber(file_dir, filename)
        
        print("PDFPLUMBER: task completed")