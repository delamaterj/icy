from flask import jsonify, request
from app.modules.datasets.services.dataset_service import DatasetService

dataset_service = DatasetService()


def upload_controller():
    file = request.files.get("file")
    response = dataset_service.upload_dataset(file)
    return jsonify(response), 200

def get_datasets_controller():
    datasets = dataset_service.get_all_datasets()
    return jsonify(datasets), 200

def get_dataset_controller(dataset_id):
    dataset = dataset_service.get_dataset_by_id(
        dataset_id
    )
    if dataset is None:
        return jsonify({"error": "Dataset not found"}), 404
    return jsonify(dataset), 200