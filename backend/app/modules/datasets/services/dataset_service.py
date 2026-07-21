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