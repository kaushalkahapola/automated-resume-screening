import numpy as np
from typing import List, Dict

def calculate_cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

def score_resumes(resume_embeddings: List[List[float]], job_desc_embedding: List[float], filenames: List[str]) -> Dict[str, float]:
    return {filename: calculate_cosine_similarity(resume_embedding, job_desc_embedding) 
            for resume_embedding, filename in zip(resume_embeddings, filenames)}