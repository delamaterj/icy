from app.modules.datasets.repo.dataset_repo import DatasetRepository
import os
from flask import current_app

class DatasetService:

    def __init__(self):
        self.dataset_repository = DatasetRepository()

    def upload_dataset(self, file):
        self.dataset_repository.upload()

        upload_folder = current_app.config["UPLOAD_FOLDER"]
        destination = os.path.join(
            upload_folder,
            file.filename
        )

        file.save(destination)
        
        return {
            "message": "File uploaded successfully.",
            "filename": file.filename
        }