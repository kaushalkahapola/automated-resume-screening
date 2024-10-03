import streamlit as st
import requests

st.title("Resume Scoring Application")

# Input for job title
job_title = st.text_input("Job Title")

# Input for job skills (comma-separated)
job_skills = st.text_input("Job Skills (comma-separated)")

# File uploader for resume
uploaded_file = st.file_uploader("Upload Resume", type=["txt", "pdf"])

if st.button("Score Resume"):
    if not job_title or not job_skills or not uploaded_file:
        st.error("Please provide job title, job skills, and upload a resume.")
    else:
        job_desc = {
            "title": job_title,
            "skills": job_skills.split(",")
        }

        files = {
            'file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
        }

        params = {
            "title": job_title,
            "skills": job_skills.split(",")
        }

        response = requests.post(
            "http://localhost:8000/upload_resume/",
            files=files,
            params=params
        )

        if response.status_code == 200:
            result = response.json()
            st.success(f"Resume Score: {result['score']}")
        else:
            st.error(f"Error scoring resume. Please try again. : {response.json()}")
