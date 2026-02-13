from fastapi import APIRouter, UploadFile, File
import shutil
import os
from uuid import uuid4

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/contest/upload")
async def upload_video(file: UploadFile = File(...)):
    file_ext = file.filename.split(".")[-1]
    unique_name = f"{uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Upload successful",
        "file_url": f"/uploads/{unique_name}"
    }
