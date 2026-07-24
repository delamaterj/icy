from flask import Blueprint

from app.modules.datasets.controllers.dataset_controller import upload_controller, get_datasets_controller, get_dataset_controller

dataset_bp = Blueprint(
    "datasets", 
    __name__,
    url_prefix="/datasets")


@dataset_bp.post("/upload")
def upload():
    return upload_controller()

@dataset_bp.get("/")
def get_all_datasets():
    return get_datasets_controller()

@dataset_bp.get("/<uuid:dataset_id>")
def get_one(dataset_id):
    return get_dataset_controller(dataset_id)