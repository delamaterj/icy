from flask import jsonify, request
from app.modules.experiments.service.experiment_service import ExperimentService

experiment_service = ExperimentService()

def create_experiment_controller():
    data = request.get_json()
    response = experiment_service.create_experiment_service(data)
    return jsonify(response), 201

def get_experiments_controller():   
    experiments = experiment_service.get_all_experiments()
    return jsonify(experiments), 200

def get_experiment_controller(experiment_id):
    experiment = experiment_service.get_experiment_by_id(
        experiment_id
    )
    if experiment is None:
        return jsonify({"error": "Experiment not found"}), 404
    return jsonify(experiment), 200