from flask import Blueprint, request

from app.modules.training_runs.controllers.training_run_controller import (
    create_training_run_controller,
    get_training_runs_controller,
    get_training_run_controller,
    run_training_run_controller)

training_run_bp = Blueprint("training_run", __name__)

@training_run_bp.post("/experiments/<uuid:experiment_id>/runs")
def create_training_run(experiment_id):
    data = request.get_json()
    return create_training_run_controller(experiment_id, data)

@training_run_bp.get("/experiments/<uuid:experiment_id>/runs")
def get_training_runs(experiment_id):
    return get_training_runs_controller(experiment_id)

@training_run_bp.get("/experiments/<uuid:experiment_id>/runs/<uuid:training_run_id>")
def get_training_run(experiment_id, training_run_id):
    return get_training_run_controller(experiment_id, training_run_id)

@training_run_bp.post("/training-runs/<uuid:training_run_id>/run")
def run_training_run(training_run_id):
    return run_training_run_controller(training_run_id)