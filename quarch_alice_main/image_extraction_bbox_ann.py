#____________________________________________________________
# pdf image extraction and annotation
#____________________________________________________________
#6/9 currently does not work, trying to figure out how to reconcile the mistral api with pymupdf, may just scrap this overall

#pip install mistralai pdf2image Pillow fitz pydantic requests 
from pydantic import BaseModel
import os
import re
import json
import argparse
import requests
from PIL import Image
#from mistralai import Mistral
import pymupdf
MISTRAL_API_KEY = "IffIovWq8tUyBc2oinkenZXp2MeqnALs"
model = "mistral-large-latest"
MISTRAL_OCR_ENDPOINT = "https://api.mistral.ai/v1/ocr"

#client = Mistral(api_key=api_key)
MISTRAL_OCR_ENDPOINT = os.getenv("MISTRAL_OCR_ENDPOINT", "https://api.mistral.ai/v1/ocr")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
if not MISTRAL_API_KEY:
    raise RuntimeError("Environment variable MISTRAL_API_KEY is required")

HEADERS = {
    "Authorization": f"Bearer {MISTRAL_API_KEY}",
}

def call_mistral_ocr(image_path):
    """
    Call the Mistral OCR API on a single image and return JSON response.
    """
    with open(image_path, "rb") as f:
        files = {"file": f}
        resp = requests.post(MISTRAL_OCR_ENDPOINT, headers=HEADERS, files=files)
    resp.raise_for_status()
    return resp.json()

def process_pdf(pdf_path, output_dir):
    """
    Render a PDF to images using PyMuPDF, run OCR, crop problem regions and save them.
    Returns list of metadata dicts for each problem image.
    """
    pdf_title = os.path.splitext(os.path.basename(pdf_path))[0]
    doc = pymupdf.open(pdf_path)
    results = []

    for page_num, page in enumerate(doc, start=1):
        # Render page to PNG
        pix = page.get_pixmap()
        temp_img_path = os.path.join(output_dir, f"{pdf_title}_page_{page_num}.png")
        pix.save(temp_img_path)

        # Open rendered image for cropping
        page_img = Image.open(temp_img_path)

        # OCR annotations
        data = call_mistral_ocr(temp_img_path)
        annotations = data.get("annotations", [])

        for ann in annotations:
            # Only process boxes labeled as 'problem'
            if ann.get("label") != "problem":
                continue

            bbox = ann.get("bbox")  # [x_min, y_min, x_max, y_max]
            if not bbox or len(bbox) != 4:
                continue

            x1, y1, x2, y2 = map(int, bbox)
            crop = page_img.crop((x1, y1, x2, y2))

            text = ann.get("text", "")
            # Extract problem number from text (e.g., "Problem 3")
            m = re.search(r"Problem\s*(\d+)", text, re.IGNORECASE)
            prob_num = m.group(1) if m else f"p{page_num}_{ann.get('id', '0')}"

            img_filename = f"{pdf_title}_problem_{prob_num}.png"
            img_path = os.path.join(output_dir, img_filename)
            crop.save(img_path)

            results.append({
                "pdf_title": pdf_title,
                "problem_number": prob_num,
                "image_path": img_path
            })

        # Clean up temp page image
        os.remove(temp_img_path)

    return results


def main(input_folder, output_folder, json_output):
    os.makedirs(output_folder, exist_ok=True)
    all_meta = []

    for fname in os.listdir(input_folder):
        if not fname.lower().endswith(".pdf"):
            continue
        pdf_file = os.path.join(input_folder, fname)
        meta = process_pdf(pdf_file, output_folder)
        all_meta.extend(meta)

    # Write out JSON metadata
    with open(json_output, "w") as jf:
        json.dump(all_meta, jf, indent=2)

    print(f"Extracted {len(all_meta)} problem images. Metadata saved to {json_output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract problem images from PDFs using Mistral OCR bounding boxes without pdf2image"
    )
    parser.add_argument("input_folder", help="Folder containing PDF files")
    parser.add_argument("output_folder", help="Folder to save extracted images")
    parser.add_argument("json_output", help="Path for the JSON metadata output")
    args = parser.parse_args()
    main(args.input_folder, args.output_folder, args.json_output)