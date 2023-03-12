import os
from pathlib import Path

from pydantic import BaseModel

from app.config import settings


class FilesService:
    class GetFilesRes(BaseModel):
        files: list[str]

    def get_files(self) -> GetFilesRes:
        upload_folder = settings.UPLOAD_FOLDER
        (_, _, filenames) = next(os.walk(upload_folder))
        find_result = self.GetFilesRes(files=filenames)
        return find_result

    class DeleteFileParams(BaseModel):
        name: str

    def delete_file(self, params: DeleteFileParams) -> None:
        upload_folder = settings.UPLOAD_FOLDER
        file_path = Path(upload_folder, params.name)
        if file_path.exists():
            file_path.unlink()
