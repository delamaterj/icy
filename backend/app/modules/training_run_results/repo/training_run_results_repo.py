from app.extensions import db
from app.models.training_run_results import TrainingRunResult


class TrainingRunResultRepository:

    @staticmethod
    def get_by_training_run_id(training_run_id):

        return TrainingRunResult.query.filter_by(
            training_run_id=training_run_id
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