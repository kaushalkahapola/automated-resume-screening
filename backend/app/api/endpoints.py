from fastapi import APIRouter, UploadFile, File, Depends, Form
from app.utils.text_extraction import extract_text
from app.services.embedding import generate_embedding
from app.models.job import JobDescription
from app.utils.scoring import score_resumes
from typing import List

router = APIRouter()

@router.post("/upload_resume/")
async def upload_resume(
    title: str = Form(...),
    skills: str = Form(...),
    description: str = Form(...),
    files: List[UploadFile] = File(...)
):
    # Create JobDescription object from form data
    job_desc = JobDescription(title=title, skills=skills.split(','), description=description)

    # Extract text from the uploaded resume files
    resume_texts = [extract_text(file) for file in files]
    
    # Generate embeddings for the resume texts
    resume_embeddings = [generate_embedding(resume_text) for resume_text in resume_texts]
    
    # Generate embedding for the job description
    job_desc_embedding = generate_embedding(job_desc.title + " " + " ".join(job_desc.skills) + " " + job_desc.description)
    
    # Get filenames
    filenames = [file.filename for file in files]
    
    # Calculate similarity scores
    similarity_scores = score_resumes(resume_embeddings, job_desc_embedding, filenames)
    print(similarity_scores)
    
    return {
        # "resume_embeddings": {filename: embedding for filename, embedding in zip(filenames, resume_embeddings)},
        # "job_description_embedding": job_desc_embedding,
        "similarity_scores": similarity_scores
    }