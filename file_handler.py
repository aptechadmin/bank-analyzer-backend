import os
from fastapi import UploadFile

async def handle_file(file: UploadFile):
    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    # process the file...
    os.remove(file_path)
    return {"status": "processed"}
