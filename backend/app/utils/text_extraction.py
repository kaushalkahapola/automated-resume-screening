from fastapi import UploadFile
import fitz  # PyMuPDF

def extract_text(file: UploadFile) -> str:
    content = file.file.read()
    if file.content_type == "application/pdf":
        text = extract_text_from_pdf(content)
    else:
        text = content.decode("utf-8")
    return text

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text
