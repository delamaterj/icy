from flask import Blueprint

from app.modules.training_runs.controllers.training_run_controller import create_training_run_controller

training_run_bp = Blueprint("training_run", __name__)

@training_run_bp.post("/experiments/<uuid:experiment_id>/runs")
def create_training_run(experiment_id):
    return create_training_run_controller(experiment_id)