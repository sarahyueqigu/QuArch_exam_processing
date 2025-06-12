from mistralai import Mistral
import os

api_key = "6kH3nw0ytZnYPrjHF7Pk2WPpLeCjIqMx"
os.environ["mistral_api_key"] = api_key

client = Mistral(api_key=api_key)

uploaded_pdf = client.files.upload(
    file={
        "file_name": "/Users/aliceguo/Documents/QuArch_exam_processing/single_page.pdf",
        "content": open("/Users/aliceguo/Documents/QuArch_exam_processing/single_page.pdf", "rb"),
    },
    purpose="ocr"
)  

signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": signed_url.url,
    },
    include_image_base64=True
)

print(ocr_response)