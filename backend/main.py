from fastapi import FastAPI, File, UploadFile, Depends, Query
from pydantic import BaseModel, Field
from typing import List
import re

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

class JobDescription(BaseModel):
    title: str = Field(...)
    skills: List[str] = Field (Query(...))

def extract_text(file: UploadFile):
    content = file.file.read().decode("utf-8")
    # print("Extracted text:", content)  # Debug print
    return content

def score_resume(resume_text: str, job_desc: JobDescription):
    # print("Job Description:", job_desc)  # Debug print
    score = 0
    # we have split the skills by comma, so we can iterate over them
    # skills = job_desc.skills[0].split(",")
    # print("Skills:", skills)  # Debug print
    for skill in job_desc.skills:
        # print(f"Checking for skill: {skill}")  # Debug print
        if re.search(r'\b' + re.escape(skill) + r'\b', resume_text, re.IGNORECASE):
            score += 1
    return score

@app.post("/upload_resume/")
async def upload_resume(job_desc: JobDescription = Depends(), file: UploadFile = File(...)):
    resume_text = extract_text(file)
    score = score_resume(resume_text, job_desc)
    return {"score": score}
