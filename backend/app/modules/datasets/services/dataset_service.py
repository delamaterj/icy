from app.modules.datasets.utils.file_storage import FileStorage
from app.modules.datasets.utils.checksum import ChecksumGenerator
from app.modules.datasets.utils.dataset_parser import DatasetParser
from app.modules.datasets.repo.dataset_repo import DatasetRepository
from app.enums.dataset_status import DatasetStatus
from app.models.dataset import Dataset


class DatasetService:

    def __init__(self):
        self.dataset_repository = DatasetRepository()

    def upload_dataset(self, file):

        stored_file = FileStorage.save(file)

        checksum = ChecksumGenerator.generate(stored_file["file_path"])

        metadata = DatasetParser.extract_metadata(stored_file["file_path"])

        dataset = Dataset(
            original_filename=file.filename,
            stored_filename=stored_file["stored_filename"],
            file_path=stored_file["file_path"],
            file_size_bytes=file.content_length,
            checksum=checksum,
            file_type="CSV",
            row_count=metadata["row_count"],
            column_count=metadata["column_count"],
            status=DatasetStatus.READY
        )

        saved_dataset = self.dataset_repository.create(
            dataset
        )

        return {
            "message": "Dataset uploaded successfully.",
            "dataset_id": str(saved_dataset.id),
            "filename": saved_dataset.original_filename,
            "status": saved_dataset.status.value
        }

    def get_all_datasets(self):

        datasets = self.dataset_repository.get_all()

        return [
            self.serialize_dataset(dataset)
            for dataset in datasets
        ]
    
    def get_dataset_by_id(self, dataset_id):

        dataset = self.dataset_repository.get_by_id(
            dataset_id
        )

        if dataset is None:
            return None

        return self.serialize_dataset(dataset)


    def serialize_dataset(self, dataset):

        return {
            "id": str(dataset.id),
            "original_filename": dataset.original_filename,
            "stored_filename": dataset.stored_filename,
            "file_type": dataset.file_type.value,
            "file_size_bytes": dataset.file_size_bytes,
            "checksum": dataset.checksum,
            "row_count": dataset.row_count,
            "column_count": dataset.column_count,
            "status": dataset.status.value,
            "uploaded_at": dataset.uploaded_at.isoformat()
        }