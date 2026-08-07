from app.extensions import db
from app.models.experiment import Experiment


class ExperimentRepository:

    def create(self, experiment: Experiment) -> Experiment:

        db.session.add(experiment)
        db.session.commit()
        db.session.refresh(experiment)

        return experiment

    def get_all(self):

        return Experiment.query.all()

    def get_by_id(self, id):

        return Experiment.query.get(id)