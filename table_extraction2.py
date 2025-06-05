import os
import pdfplumber
from pdf2image import convert_from_path
from PIL import Image

# 1. Configuration
PDF_PATH = "input.pdf"          # Path to your PDF file
OUTPUT_DIR = "tables_output"    # Folder where cropped-table images will be saved
DPI = 300                       # Rendering resolution; higher → sharper crop
MIN_TABLE_WIDTH = 50            # Minimum width (in PDF points) to consider a detected "table"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 2. Open the PDF with pdfplumber
with pdfplumber.open(PDF_PATH) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        # 2a. Detect table objects on this page
        # pdfplumber’s `extract_tables()` returns the table data,
        # but `page.find_tables()` returns Table objects with bbox info.
        tables = page.find_tables()

        # If no tables found, skip this page
        if not tables:
            continue

        # 2b. Render this page to a PIL image at the specified DPI
        # pdf2image’s convert_from_path returns a list of PIL Images—in page order
        # We only need the single page, so index by page_number-1.
        images = convert_from_path(PDF_PATH, dpi=DPI, first_page=page_number, last_page=page_number)
        page_img = images[0]  # PIL.Image of the rendered page

        # PDF coordinate system: (0, 0) is at bottom‐left; pdfplumber returns bbox = (x0, y0, x1, y1)
        # in PDF points (1 point = 1/72 inch). At DPI=300, 1 PDF point → (300/72) ≈ 4.1667 pixels.

        scale = DPI / 72.0  # multiplier from PDF points → image pixels

        # 3. Loop through each detected table, crop and save
        for tbl_index, tbl in enumerate(tables, start=1):
            x0, y0, x1, y1 = tbl.bbox  # bbox in PDF points

            width_pts = x1 - x0
            height_pts = y1 - y0
            # (Optional) Skip tiny “tables” that are likely false positives
            if width_pts < MIN_TABLE_WIDTH:
                continue

            # Convert PDF‐points bbox → pixel bbox:
            #    - In PDF: origin (0,0) is bottom-left. In PIL: origin (0,0) is top-left.
            #    - So pixel_y_top = (page_height_pts - y1) * scale
            #    - pixel_y_bottom = (page_height_pts - y0) * scale
            page_width_pts = page.width
            page_height_pts = page.height

            # Compute pixel coords
            px_x0 = int(x0 * scale)
            px_x1 = int(x1 * scale)
            # For Y: invert PDF’s bottom-left origin to image’s top-left origin
            px_y_top = int((page_height_pts - y1) * scale)
            px_y_bottom = int((page_height_pts - y0) * scale)

            # Crop the region from the PIL image
            # Box = (left, upper, right, lower) in pixels
            crop_box = (px_x0, px_y_top, px_x1, px_y_bottom)
            table_img = page_img.crop(crop_box)

            # Save out as PNG (or JPG, etc.)
            out_filename = os.path.join(
                OUTPUT_DIR,
                f"page_{page_number:03d}_table_{tbl_index:02d}.png"
            )
            table_img.save(out_filename)
            print(f"Saved table crop → {out_filename}")