from flask import Blueprint
from app.modules.experiments.controllers.experiment_controller import create_experiment_controller

experiment_bp = Blueprint(
    "experiments", 
    __name__,
    url_prefix="/experiments")

@experiment_bp.post("/upload")
def upload():
    return create_experiment_controller()

