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

    def get_by_experiment_id(self, experiment_id):

        return TrainingRun.query.filter_by(
            experiment_id=experiment_id
        ).all()

    def get_by_id(self, run_id):

        return TrainingRun.query.filter_by(
            id=run_id
        ).first()

    def update_status(self, run_id, status):

        run = TrainingRun.query.filter_by(
            id=run_id
        ).first()

        if not run:
            return None

        run.status = status
        db.session.commit()

        return run

    def update_error_message(self, run_id, message):
    
            run = TrainingRun.query.filter_by(
                id=run_id
            ).first()
    
            if not run:
                return None
    
            run.error_message = message
            db.session.commit()
    
            return run
