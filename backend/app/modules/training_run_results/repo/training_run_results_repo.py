from app.extensions import db
from app.models.training_run_results import TrainingRunResult
from app.models.training_run import TrainingRun

class TrainingRunResultRepository:

    @staticmethod
    def get_by_experiment_id(experiment_id):
        return TrainingRun.query.filter_by(
            experiment_id=experiment_id
        ).all()

    @staticmethod
    def get_by_id(run_id):
        return TrainingRun.query.filter_by(
            id=run_id
        ).first()

    @staticmethod
    def create_result(
        training_run_id,
        accuracy,
        precision,
        recall,
        f1_score,
        confusion_matrix
    ):

        result = TrainingRunResult(
            training_run_id=training_run_id,
            accuracy=accuracy,
            precision=precision,
            recall=recall,
            f1_score=f1_score,
            confusion_matrix=confusion_matrix
        )

        db.session.add(result)
        db.session.commit()

        return result