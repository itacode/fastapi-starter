import re
from http import HTTPStatus
from pathlib import Path

from fastapi import APIRouter, HTTPException, UploadFile
from pydantic import BaseModel

from app.api.endpoints.files.files_service import FilesService
from app.config import settings

router = APIRouter()
_files_service = FilesService()


def get_valid_filename(s) -> str:
    """
    Return the given string converted to a string that can be used for a clean
    filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot.
    >>> get_valid_filename("john's portrait in 2004.jpg")
    'johns_portrait_in_2004.jpg'
    """
    s = str(s).strip().replace(" ", "_")
    return re.sub(r"[^-\w.]", "", s)


@router.get("/files/")
def get_files() -> FilesService.GetFilesRes:
    result = _files_service.get_files()
    return result


class UploadFileBody(BaseModel):
    file: UploadFile


@router.post("/files/")
async def upload_file(body: UploadFileBody):
    file = body.file
    if file.filename == "" or file.filename is None:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="No selected file")
    filename = get_valid_filename(file.filename)
    with open(Path(settings.UPLOAD_FOLDER, filename), "wb") as out_file:
        file_bytes = await file.read()
        out_file.write(file_bytes)
        await file.close()
    return filename


@router.delete("/files/{name}")
def delete_file(name: str):
    params = _files_service.DeleteFileParams(name=name)
    _files_service.delete_file(params=params)
    return "OK"
