from fastapi import APIRouter, UploadFile, File, Depends
from app.utils.text_extraction import extract_text
from app.services.embedding import generate_embedding
from app.models.job import JobDescription
from app.utils.scoring import score_resumes
from typing import List

router = APIRouter()

@router.post("/upload_resume/")
async def upload_resume(job_desc: JobDescription = Depends(), files: List[UploadFile] = File(...)):
    # Extract text from the uploaded resume files
    resume_texts = [extract_text(file) for file in files]
    
    # Generate embeddings for the resume texts
    resume_embeddings = [generate_embedding(resume_text) for resume_text in resume_texts]
    
    # Generate embedding for the job description
    job_desc_embedding = generate_embedding(job_desc.title + " " + " ".join(job_desc.skills) + " " + job_desc.description)
    
    # Calculate similarity scores
    similarity_scores = score_resumes(resume_embeddings, job_desc_embedding)
    
    return {
        "resume_embeddings": resume_embeddings,
        "job_description_embedding": job_desc_embedding,
        "similarity_scores": similarity_scores
    }