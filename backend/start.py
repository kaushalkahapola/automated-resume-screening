import uvicorn
from main import app  # Ensure this imports your FastAPI app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(8000))
