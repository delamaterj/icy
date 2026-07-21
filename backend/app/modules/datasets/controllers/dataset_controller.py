from flask import jsonify, request
from app.modules.datasets.services.dataset_service import DatasetService
import os

dataset_service = DatasetService()


def upload_controller():
    file = request.files.get("file")
    response = dataset_service.upload_dataset(file)

    return jsonify(response), 200