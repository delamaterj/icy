from flask import jsonify
from app.modules.training_runs.services.training_run_services import (
    TrainingRunService
)

def serialize_training_run(run):

    return {
        "id": str(run.id),
        "experiment_id": str(run.experiment_id),
        "status": run.status.value,
        "started_at": (
            run.started_at.isoformat()
            if run.started_at
            else None
        ),
        "completed_at": (
            run.completed_at.isoformat()
            if run.completed_at
            else None
        ),
        "created_at": run.created_at.isoformat()
    }

def serialize_training_run_details(run):

    return {
        "id": str(run.id),
        "experiment_id": str(run.experiment_id),
        "status": run.status.value,
        "started_at": (
            run.started_at.isoformat()
            if run.started_at
            else None
        ),
        "completed_at": (
            run.completed_at.isoformat()
            if run.completed_at
            else None
        ),
        "created_at": run.created_at.isoformat(),
        "result": {
            "accuracy": run.result.accuracy,
            "precision": run.result.precision,
            "recall": run.result.recall,
            "f1_score": run.result.f1_score,
            "confusion_matrix": run.result.confusion_matrix
        }
    }

training_run_service = TrainingRunService()

def create_training_run_controller(experiment_id):

    response = training_run_service.create_training_run(
        experiment_id
    )
    return jsonify(response), 201

def get_training_runs_controller(experiment_id):

    runs = training_run_service.get_runs_by_experiment(
        experiment_id
    )

    return jsonify([
        serialize_training_run(run)
        for run in runs
    ]), 200

def get_training_run_controller(
    experiment_id,
    run_id
):

    run = training_run_service.get_run(
        experiment_id,
        run_id
    )

    return jsonify(
        serialize_training_run_details(run)
    ), 200