import os
import uuid
from flask import current_app
from app.common.exceptions import StorageException


class FileStorage:

    @staticmethod
    def save(file):

        try:
            extension = os.path.splitext(file.filename)[1]

            stored_filename = (
                f"{uuid.uuid4()}{extension}"
            )

            upload_folder = current_app.config["UPLOAD_FOLDER"]

            file_path = os.path.join(
                upload_folder,
                stored_filename
            )

            file.save(file_path)

            return {
                "stored_filename": stored_filename,
                "file_path": file_path
            }
        except OSError:
            raise StorageException("Unable to save uploaded file.")

    @staticmethod
    def delete(file_path: str):

        if os.path.exists(file_path):
            os.remove(file_path)