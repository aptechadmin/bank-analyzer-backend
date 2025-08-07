from fastapi import FastAPI, UploadFile, File
from file_handler import handle_file
app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return await handle_file(file)
