from fastapi import FastAPI, UploadFile, File, HTTPException
from app.inference import detect_banknote
import shutil
import os

app = FastAPI(title="Taka Detection API")

@app.get("/")
def root():
    return {"message": "API is running. Go to /docs for the upload UI."}

@app.post("/predict")
# 'File(...)' is what creates the "Choose File" button in Swagger
async def predict(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image.")

    temp_path = f"temp_{file.filename}"
    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Run detection
        result = detect_banknote(temp_path)
        return result
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)