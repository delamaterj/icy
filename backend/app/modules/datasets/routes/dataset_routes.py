from flask import Blueprint

from app.modules.datasets.controllers.dataset_controller import upload_controller

dataset_bp = Blueprint(
    "datasets", 
    __name__,
    url_prefix="/datasets")


@dataset_bp.post("/upload")
def upload():
    return upload_controller()