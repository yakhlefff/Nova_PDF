from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

from services.replace_service import replace_text
from services.markup_service import highlight_text
from services.overlay_service import add_text_overlay

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.get("/")
def root():
    return {"message": "NovaPDF backend running"}


@app.post("/replace-text")
async def replace_text_api(
    file: UploadFile = File(...),
    old_text: str = "",
    new_text: str = ""
):
    input_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = os.path.join(OUTPUT_DIR, "replaced_" + file.filename)

    replace_text(input_path, output_path, old_text, new_text)

    return FileResponse(output_path)


@app.post("/highlight")
async def highlight_api(
    file: UploadFile = File(...),
    text: str = ""
):
    input_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = os.path.join(OUTPUT_DIR, "highlight_" + file.filename)

    highlight_text(input_path, output_path, text)

    return FileResponse(output_path)


@app.post("/add-text")
async def add_text_api(
    file: UploadFile = File(...),
    text: str = "",
    x: float = 50,
    y: float = 50
):
    input_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = os.path.join(OUTPUT_DIR, "overlay_" + file.filename)

    add_text_overlay(input_path, output_path, text, x, y)

    return FileResponse(output_path)
