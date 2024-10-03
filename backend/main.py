from fastapi import FastAPI, File, UploadFile, Depends, Query
from pydantic import BaseModel, Field
from typing import List
import re
import fitz  # PyMuPDF

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

class JobDescription(BaseModel):
    title: str = Field(...)
    skills: List[str] = Field(Query(...))

def extract_text(file: UploadFile):
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

def score_resume(resume_text: str, job_desc: JobDescription):
    score = 0
    for skill in job_desc.skills:
        if re.search(r'\b' + re.escape(skill) + r'\b', resume_text, re.IGNORECASE):
            score += 1
    return score

@app.post("/upload_resume/")
async def upload_resume(job_desc: JobDescription = Depends(), file: UploadFile = File(...)):
    resume_text = extract_text(file)
    score = score_resume(resume_text, job_desc)
    return {"score": score}
