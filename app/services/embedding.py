import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def generate_embedding(text, model="models/text-embedding-004", output_dimensionality=10):
    result = genai.embed_content(model=model, content=text, output_dimensionality=output_dimensionality)
    return result["embedding"]
