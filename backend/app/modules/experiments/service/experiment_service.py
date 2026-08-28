from app.models.dataset import DatasetStatus
from app.models.experiment import Experiment, ExperimentStatus

from app.modules.datasets.repo.dataset_repo import DatasetRepository
from app.modules.experiments.repo.experiment_repo import ExperimentRepository
from app.modules.experiments.utils.experiment_validation import ExperimentValidation
from app.modules.datasets.utils.dataset_parser import DatasetParser

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
            if errors["errors"]:
                raise ValidationException(errors)

            dataset = self.dataset_repository.get_by_id(
                data["dataset_id"]
            )
            if dataset is None:
                raise ResourceNotFoundException(
                    "Dataset not found."
                )

            metadata = DatasetParser.extract_metadata( dataset.file_path ) 
            columns = metadata["columns"] 
            target_column = data["target_column"] 
            if target_column not in columns: 
                raise ValidationException([ f"Target column '{target_column}' " "does not exist in the selected dataset." ])

            '''if dataset.status != DatasetStatus.READY:
                raise ValidationException(
                    ["Dataset must be READY before creating an experiment."]
                )'''

            experiment = Experiment( 
                dataset_id=dataset.id, 
                name=data["name"], 
                description=data.get("description"), 
                status=ExperimentStatus.CREATED, 
                model=data["model"], 
                target_column=data["target_column"], 
                #test_size=data.get("test_size"), 
                #random_seed=data.get("random_seed") 
            )

            experiment = self.experiment_repository.create(experiment)

            return {
                "id": str(experiment.id),
                "dataset_id": str(dataset.id),
                "name": experiment.name,
                "status": experiment.status.value,
                "model": experiment.model.value,
                "created_at": experiment.created_at
            }

        except AppException:
            raise
        except Exception:
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
                    "model": experiment.model.value,
                    "status": experiment.status.value,
                    "created_at": experiment.created_at,
                    "target_column": experiment.target_column,
                    #"test_size": experiment.test_size,
                    #"random_seed": experiment.random_seed,
                }
            
            except Exception as e:
                print(e)
                raise AppException(f"Could not get experiment {experiment_id}.")

    def serialize_summary(self, experiment):
    
            return {
                "id": str(experiment.id),
                "name": experiment.name,
                "model": experiment.model.value,
                "dataset_id": experiment.dataset_id,
                "status": experiment.status.value,
                "created_at": experiment.created_at
            }