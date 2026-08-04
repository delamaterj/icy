from app.models.dataset import DatasetStatus
from app.models.experiment import Experiment, ExperimentStatus

from app.modules.datasets.repo.dataset_repo import DatasetRepository
from app.modules.experiments.repo.experiment_repo import ExperimentRepository
from app.modules.experiments.utils.experiment_validation import ExperimentValidation

from app.common.exceptions import (
    ValidationException,
    ResourceNotFoundException,
    AppException
)

class ExperimentService:

    def __init__(self):

        self.dataset_repository = DatasetRepository()
        self.experiment_repository = ExperimentRepository()

    def create_experiment_service(self, data):

        try:

            errors = ExperimentValidation.validate_create(data)
            if errors:
                raise ValidationException(errors)

            dataset = self.dataset_repository.get_by_id(
                data["dataset_id"]
            )
            if dataset is None:
                raise ResourceNotFoundException(
                    "Dataset not found."
                )

            if dataset.status != DatasetStatus.READY:
                raise ValidationException(
                    ["Dataset must be READY before creating an experiment."]
                )

            experiment = Experiment(
                dataset_id=dataset.id,
                name=data["name"],
                description=data.get("description"),
                status=ExperimentStatus.CREATED,
            )

            experiment = self.experiment_repository.create(experiment)

            return {
                "experiment_id": str(experiment.id),
                "dataset_id": str(dataset.id),
                "name": experiment.name,
                "status": experiment.status.value,
            }

        except AppException:
            raise
        except Exception as e:
            print(e)
            raise AppException("Could not upload experiment.")

    def get_all_experiments(self):
        try:
            experiments = self.experiment_repository.get_all()
            return [
                self.serialize_summary(experiment)
                for experiment in experiments
            ]
        except Exception:
            raise AppException("Could not get experiments.")

    def get_experiment_by_id(self, experiment_id):
            try:
                experiment = self.experiment_repository.get_by_id(
                    experiment_id
                )
    
                if experiment is None:
                    return None
    
                return {
                    "id": str(experiment.id),
                    "name": experiment.name,
                    "dataset_id": str(experiment.dataset_id),
                    "description": experiment.description,
                    "status": experiment.status.value,
                    "created at": experiment.created_at,
                    "started at": experiment.started_at,
                    "completed at": experiment.completed_at
                }
            
            except Exception as e:
                print(e)
                raise AppException(f"Could not get experiment {experiment_id}.")

    def serialize_summary(self, experiment):
    
            return {
                "id": str(experiment.id),
                "name": experiment.name,
                "dataset_id": experiment.dataset_id,
                "status": experiment.status.value
            }