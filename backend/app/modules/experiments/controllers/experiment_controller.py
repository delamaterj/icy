from flask import jsonify, request
from app.modules.experiments.service.experiment_service import ExperimentService

experiment_service = ExperimentService()

def create_experiment_controller():
    data = request.get_json()
    response = experiment_service.create_experiment_service(data)
    return jsonify(response), 201