# HireLens Backend

This is the backend for the HireLens application, built with FastAPI. The backend is designed to handle job descriptions, resumes, and embedding generation to provide powerful recommendations and evaluations.

[HireLens Web Application](https://github.com/kaushalkahapola/hire-lens)

## Table of Contents

- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Endpoints](#endpoints)
- [Machine Learning Approach](#machine-learning-approach)
- [Embedding Generation](#embedding-generation)
  
## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.7+.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **Google Generative AI**: For generating text embeddings.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Setup

### Prerequisites

- Python 3.7 or higher
- pip
- A Google Generative AI API key

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/kaushalkahapola/automated-resume-screening
   cd automated-resume-screening
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the backend directory and add your Google Generative AI API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. Run the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

Your backend should now be running at `http://localhost:8000`.

## Endpoints

### 1. Upload Resume

**POST** `/upload_resume/`

- **Request Body**: 
  - `files`: List of PDF files (resumes).
  - `title`: Job title (string).
  - `skills`: List of skills (array of strings).
  - `description`: Job description (string).

- **Response**: JSON response containing the results of the processing.

## Machine Learning Approach

The HireLens backend employs several machine learning approaches to analyze and recommend based on job descriptions and resumes:

1. **Text Extraction**: 
   - Extract text from uploaded PDF resumes using PyMuPDF or a similar library.

2. **Embedding Generation**:
   - Utilize Google Generative AI to generate embeddings for both job descriptions and resume contents. This allows for semantic similarity comparisons, helping to match candidates to job roles effectively.

3. **Similarity Scoring**:
   - Calculate cosine similarity between job description embeddings and resume embeddings to evaluate the relevance of candidates to job postings.

## Embedding Generation

Embedding generation is achieved using the Google Generative AI API. Here’s an example of how embeddings are generated:

```python
import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Example text for embedding
text = "Hello World!"
result = genai.embed_content(
    model="models/text-embedding-004", content=text, output_dimensionality=10
)
print(result["embedding"])
```

---
