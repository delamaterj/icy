from app.extensions import db
from app.models.experiment import Experiment


class ExperimentRepository:

    def create(self, experiment: Experiment) -> Experiment:

        db.session.add(experiment)
        db.session.commit()
        db.session.refresh(experiment)

        return experiment