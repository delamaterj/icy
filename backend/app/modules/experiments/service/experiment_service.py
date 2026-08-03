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