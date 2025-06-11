import os
from mistralai import Mistral, DocumentURLChunk, ImageURLChunk, ResponseFormat
from mistralai.extra import response_format_from_pydantic_model

api_key = "6kH3nw0ytZnYPrjHF7Pk2WPpLeCjIqMx"
os.environ["mistral_api_key"] = api_key

client = Mistral(api_key=api_key)

uploaded_pdf = client.files.upload(
    file={
        "file_name": "data/one_page.pdf",
        "content": open("data/one_page.pdf", "rb"),
    },
    purpose="ocr"
)  

signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)

# ocr_response = client.ocr.process(
#     model="mistral-ocr-latest",
#     document={
#         "type": "document_url",
#         "document_url": signed_url.url,
#     },
#     include_image_base64=True
# )

# print(ocr_response)

from pydantic import BaseModel

# Document Annotation response format
class Document(BaseModel):
  language: str
  chapter_titles: list[str]
  urls: list[str]
  
# Client call
response = client.ocr.process(
    model="mistral-ocr-latest",
    pages=list(range(8)),
    document={
        "type": "document_url",
        "document_url": signed_url.url,
    },
    document_annotation_format=response_format_from_pydantic_model(Document),
    include_image_base64=True
  )

print(response)