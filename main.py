# from fastapi import FastAPI, File, UploadFile, Depends, Query, HTTPException
# from pydantic import BaseModel, Field
# from typing import List
# import re
# import fitz  # PyMuPDF

# app = FastAPI()

# # Root endpoint for testing
# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# # Job description model, including job title and required skills
# class JobDescription(BaseModel):
#     title: str = Field(..., description="Title of the job")
#     skills: List[str] = Field(Query(...), description="List of required skills")

# # Function to extract text from an uploaded file (currently supports PDF)
# def extract_text(file: UploadFile):
#     content = file.file.read()
#     if file.content_type == "application/pdf":
#         text = extract_text_from_pdf(content)
#     else:
#         raise HTTPException(status_code=400, detail="Unsupported file type. Only PDFs are supported.")
#     return text

# # Helper function to extract text from a PDF file using PyMuPDF (fitz)
# def extract_text_from_pdf(pdf_bytes: bytes) -> str:
#     pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
#     text = ""
#     for page_num in range(pdf_document.page_count):
#         page = pdf_document.load_page(page_num)
#         text += page.get_text()
#     return text

# # Endpoint to accept job description and PDF resumes, and print content
# @app.post("/upload_resumes/")
# async def upload_resumes(
#     job_desc: JobDescription = Depends(), 
#     files: List[UploadFile] = File(...)
# ):
#     # Print the job description details
#     print("Job Title:", job_desc.title)
#     print("Required Skills:", ", ".join(job_desc.skills))

#     resume_texts = []

#     for file in files:
#         # Extract text from each uploaded resume
#         resume_text = extract_text(file)
#         resume_texts.append(resume_text)

#         # Print the extracted resume content
#         print(f"Resume ({file.filename}) Content:")
#         print(resume_text)

#     return {
#         "job_description": {
#             "title": job_desc.title,
#             "skills": job_desc.skills
#         },
#         "resumes": [{
#             "filename": file.filename,
#             "content": resume_text
#         } for file, resume_text in zip(files, resume_texts)]
#     }
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
load_dotenv()

# Now you can access your environment variables
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to HireLens!"}

# Import your embedding logic and routes
from app.api.endpoints import router as api_router

app.include_router(api_router)
