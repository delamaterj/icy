from flask import Blueprint
from app.modules.experiments.controllers.experiment_controller import create_experiment_controller, get_experiment_controller, get_experiments_controller

experiment_bp = Blueprint(
    "experiments", 
    __name__,
    url_prefix="/experiments")

@experiment_bp.post("")
def upload():
    return create_experiment_controller()

@experiment_bp.get("")
def get_all_experiments():
    return get_experiments_controller()

@experiment_bp.get("/<uuid:experiment_id>")
def get_one(experiment_id):
    return get_experiment_controller(experiment_id)

