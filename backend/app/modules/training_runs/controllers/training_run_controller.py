from flask import jsonify
from app.modules.training_runs.services.training_run_services import (
    TrainingRunService
)

training_run_service = TrainingRunService()

def create_training_run_controller(experiment_id):

    response = training_run_service.create_training_run(
        experiment_id
    )
    return jsonify(response), 201