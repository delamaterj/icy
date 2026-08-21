from app.common.exceptions import ValidationException
from app.enums.dataset_status import DatasetStatus
from app.modules.experiments.repo.experiment_repo import (
    ExperimentRepository
)
from app.modules.training_runs.repo.training_run_repo import (
    TrainingRunRepository
)

class TrainingRunService:

    def __init__(self):

        self.experiment_repository = ExperimentRepository()
        self.training_run_repository = TrainingRunRepository()


    def create_training_run(self, experiment_id):

        experiment = self.experiment_repository.get_by_id(
            experiment_id
        )

        if not experiment:
            raise ValidationException([
                "Experiment not found."
            ])

        dataset = experiment.dataset

        if not dataset:
            raise ValidationException([
                "Experiment dataset not found."
            ])

        if dataset.status != DatasetStatus.READY:
            raise ValidationException([
                "Experiment dataset must be READY."
            ])

        training_run = self.training_run_repository.create(
            experiment.id
        )

        return {
            "id": str(training_run.id),
            "experiment_id": str(training_run.experiment_id),
            "status": training_run.status.value,
            "created_at": training_run.created_at.isoformat()
        }

    def get_runs_by_experiment(experiment_id):

        runs = TrainingRunRepository.get_by_experiment_id(
            experiment_id
        )

        return runs

    def get_run(run_id):

        run = TrainingRunRepository.get_by_id(
            run_id
        )

        if not run:
            raise ValidationException([
                "Training run not found."
            ])

        return run