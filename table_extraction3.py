import pdfplumber
import math
import pymupdf
from PIL import Image
import os
import shutil

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

            # TODO: inspect this
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




if __name__ == "__main__":

    path = "../data/CDA 4205 Computer Architecture Exam 2 Practice Solution-2.pdf"
    file_pymupdf = pymupdf.open(path)
    file = pdfplumber.open(path)
    page_count = len(file.pages)

    #Extract images
    for page_number in range(page_count):
        images = file_pymupdf[page_number].get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            pix = pymupdf.Pixmap(file_pymupdf, xref)
            if pix.n < 5:  # this is GRAY or RGB
                pix.save(f"image_{page_number+1}_{img_index+1}.png")
            pix = None
        

    # Extract tables as images
    with file as pdf:

        # Extract images
        tables = detect_all_tables(path, stream_mode=False)
        print(f"Found {len(tables)} tables (lattice).")
        counter = 0
        for t in tables:
            p = t["page_num"]
            bbox = t["bbox"]
            print(f" • Page {p+1}: bbox={bbox}, cells={len(t['cells'])}")

            x1 = math.floor(bbox[0])
            y1 = math.floor(bbox[1])
            x2 = math.ceil(bbox[2])
            y2 = math.ceil(bbox[3])

            # Convert to (x, y, width, height):
            width  = x2 - x1 
            height = y2 - y1 
                
            page = pdf.pages[p]
            # pdfplumber images are PIL Image objects at 72 dpi by default
            pil_image = page.to_image(resolution=150).original  # render at 150 dpi

            # Convert box from points→pixels: scale = 150 / 72
            scale = 150/72
            left   = int(x1 * scale)
            top    = int(y1 * scale)
            right  = int(x2 * scale)
            bottom = int(y2 * scale)

            cropped = pil_image.crop((left, top, right, bottom))
            
            image_name = "cropped_region" + str(counter) + ".png"

            cropped.save(image_name)
            print("Saved ", image_name)
            counter+=1

    
    # Example 2: Stream mode (for borderless/whitespace tables)
    # tables_stream = detect_all_tables(pdf_file, stream_mode=True)
    # print(f"Found {len(tables_stream)} tables (stream).")
    # for t in tables_stream:
    #     p = t["page_num"]
    #     bbox = t["bbox"]
    #     print(f" • Page {p+1}: bbox={bbox}, cells={len(t['cells'])}")

