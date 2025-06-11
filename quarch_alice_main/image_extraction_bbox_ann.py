#____________________________________________________________
# pdf image extraction and annotation
#____________________________________________________________
#6/9 currently does not work, trying to figure out how to reconcile the mistral api with pymupdf, may just scrap this overall
#6/10 still does not work, the ocr seems to just be for extracting text from images, which is not what we want

#pip install mistralai pdf2image Pillow fitz pydantic requests 
from pydantic import BaseModel, Field
from mistralai.extra import response_format_from_pydantic_model
import os
import json
import argparse
from pathlib import Path
import pymupdf
from mistralai import Mistral

api_key = "6kH3nw0ytZnYPrjHF7Pk2WPpLeCjIqMx"
os.environ["mistral_api_key"] = api_key
client = Mistral(api_key=api_key)

def extract_images_from_pdf(pdf_path: str, image_dir: Path):
    """
    Extract all embedded images from a PDF using PyMuPDF, saving each to image_dir.
    Returns an iterator of saved image file Paths.
    """
    image_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    for page_number in range(len(doc)):
        page = doc[page_number]
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image.get("ext", "png")
            fname = f"{Path(pdf_path).stem}_pg{page_number+1}_img{img_index}.{ext}"
            out_path = image_dir / fname
            with open(out_path, "wb") as f:
                f.write(image_bytes)
            print(f"Extracted image: {out_path}")
            yield out_path


def call_mistral_ocr_image(image_path: Path):
    """
    Upload an extracted image to Mistral OCR by first wrapping it into a single-page PDF.
    Returns the OCR response object.
    """
    # Convert image to a temporary PDF in-memory
    from PIL import Image
    import io
    image_path = Path(image_path) 
    img = Image.open(image_path)
    pdf_bytes = io.BytesIO()
    img.convert("RGB").save(pdf_bytes, format="PDF")
    pdf_bytes.seek(0)

    # Upload the PDF
    upload = client.files.upload(
        file={"file_name": image_path.stem + ".pdf", "content": pdf_bytes},
        purpose="ocr"
    )
    signed = client.files.get_signed_url(file_id=upload.id)

    # Call OCR on the PDF wrapper
    resp = client.ocr.process(
        model="mistral-ocr-latest",
        document={"type": "document_url", "document_url": signed.url}
    )
    return resp


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract embedded images from PDFs and OCR-label them via Mistral"
    )
    parser.add_argument("input_path", help="PDF file or folder of PDFs to process")
    parser.add_argument("outdir", help="Directory where images and OCR results go")
    args = parser.parse_args()

    base_in = Path(args.input_path)
    base_out = Path(args.outdir)
    if base_in.is_dir():
        pdf_files = sorted(base_in.glob("*.pdf"))
    elif base_in.is_file() and base_in.suffix.lower() == ".pdf":
        pdf_files = [base_in]
    else:
        parser.error(f"Input {base_in} is not a PDF or directory of PDFs.")

    for pdf in pdf_files:
        print(f"Processing PDF: {pdf}")
        # Create folder for this PDF's images
        img_dir = base_out / pdf.stem / "extracted_images"
        for img_path in extract_images_from_pdf(str(pdf), img_dir):
            print(f"OCR on image {img_path.name}...")
            ocr_resp = call_mistral_ocr_image(str(img_path))
            # Collect text blocks
            lines = []
            for page in ocr_resp.data:
                for block in getattr(page, 'blocks', []):
                    lines.append(block.text)
            text = "\n".join(lines)
            # Save OCR text alongside image
            text_file = img_path.with_suffix('.txt')
            text_file.write_text(text, encoding='utf-8')
            print(f"Saved OCR text → {text_file}")

    print("All PDFs processed.")