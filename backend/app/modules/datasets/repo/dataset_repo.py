from app.extensions import db


class DatasetRepository:

    def create(self, dataset):

        db.session.add(dataset)
        db.session.commit()

        return dataset