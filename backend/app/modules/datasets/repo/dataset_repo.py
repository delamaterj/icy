from app.extensions import db
from app.models.dataset import Dataset
from sqlalchemy.exc import SQLAlchemyError
from app.common.exceptions import DatabaseException


class DatasetRepository:

    def create(self, dataset):
        try:
            db.session.add(dataset)
            db.session.commit()
            return dataset
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseException("Unable to save dataset.") from e

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

    def update(self, dataset):
        db.session.commit()
        return dataset