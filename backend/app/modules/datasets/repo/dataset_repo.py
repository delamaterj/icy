from app.extensions import db
from app.models.dataset import Dataset


class DatasetRepository:

    def create(self, dataset):
        db.session.add(dataset)
        db.session.commit()
        return dataset

    def get_all(self):
        return Dataset.query.all()


    def get_by_id(self, dataset_id):
        return db.session.get(
            Dataset,
            dataset_id
        )
    
    def get_by_checksum(self, checksum):
        return Dataset.query.filter_by(
            checksum=checksum
        ).first()