from app.extensions import db
from app.models.training_run import TrainingRun


class TrainingRunRepository:

    def create(self, experiment_id):

        training_run = TrainingRun(
            experiment_id=experiment_id
        )

        db.session.add(training_run)
        db.session.commit()

        return training_run