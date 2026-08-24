from app.common.exceptions import ValidationException
from app.enums.dataset_status import DatasetStatus
from app.modules.experiments.repo.experiment_repo import (
    ExperimentRepository
)
from app.modules.training_runs.repo.training_run_repo import TrainingRunRepository
from app.modules.training_run_results.repo.training_run_results_repo import TrainingRunResultRepository
from app.modules.training_runs.utils.dataset_loader import DatasetLoader
from app.modules.training_runs.utils.model_factory import ModelFactory
from app.modules.training_runs.utils.model_trainer import ModelTrainer
from app.modules.training_runs.utils.model_evaluator import ModelEvaluator
from app.enums.training_run_status import TrainingRunStatus

class TrainingRunService:

    def __init__(self):

        self.experiment_repository = ExperimentRepository()
        self.training_run_repository = TrainingRunRepository()
        self.training_run_result_repository = TrainingRunResultRepository()


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

        '''if dataset.status != DatasetStatus.READY:
            raise ValidationException([
                "Experiment dataset must be READY."
            ])'''

        training_run = self.training_run_repository.create(
            experiment.id
        )

        try:
            self.training_run_repository.update_status(
                training_run.id,
                TrainingRunStatus.RUNNING
            )

            data = DatasetLoader.load_and_split(
                file_path=dataset.file_path,
                target_column=experiment.target_column,
                test_size=experiment.test_size,
                random_seed=experiment.random_seed
            )

            model = ModelFactory.create(
                experiment.model,
                experiment.random_seed
            )

            trained_model = ModelTrainer.train(
                model,
                data["X_train"],
                data["y_train"]
            )

            results = ModelEvaluator.evaluate(
                trained_model,
                data["X_test"],
                data["y_test"]
            )

            
            self.training_run_result_repository.create_result(
                training_run_id=training_run.id,
                accuracy=results["accuracy"],
                precision=results["precision"],
                recall=results["recall"],
                f1_score=results["f1_score"],
                confusion_matrix=results["confusion_matrix"]
            )

            self.training_run_repository.update_status(
                training_run.id,
                TrainingRunStatus.COMPLETED
            )

            return {
                "id": str(training_run.id),
                "experiment_id": str(training_run.experiment_id),
                "status": training_run.status.value,
                "created_at": training_run.created_at.isoformat()
            }
        except Exception as e:

            self.training_run_repository.update_status(
                training_run.id,
                TrainingRunStatus.FAILED
            )

            self.training_run_repository.update_error_message(
                training_run.id,
                str(e)
            )

        raise ValidationException([
            "Training Run Failed."
        ])
        
    def get_runs_by_experiment(self, experiment_id):

        runs = self.training_run_repository.get_by_experiment_id(
            experiment_id
        )

        return runs

    def get_run(self, experiment_id, run_id):

        run = self.training_run_repository.get_by_id(
            run_id
        )

        if not run:
            raise ValidationException("Training run not found.")

        if run.experiment_id != experiment_id:
            raise ValidationException("Training run not found.")

        return run