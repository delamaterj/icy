from app.modules.datasets.utils.file_storage import FileStorage
from app.modules.datasets.utils.checksum import ChecksumGenerator
from app.modules.datasets.utils.dataset_parser import DatasetParser
from app.modules.datasets.repo.dataset_repo import DatasetRepository
from app.enums.dataset_status import DatasetStatus
from app.models.dataset import Dataset
from app.modules.datasets.validators.dataset_validator import DatasetValidator
from app.common.exceptions import DuplicateDatasetException, AppException, ValidationException
from app.modules.datasets.utils.file_type_detector import FileTypeDetector

class DatasetService:

    def __init__(self):
        self.dataset_repository = DatasetRepository()
        self.dataset_validator = DatasetValidator()

    def upload_dataset(self, file):
        try:

            file_type = FileTypeDetector.detect(file.filename)

            if not file_type:
                raise ValidationException([f"Unsupported file type."])

            checksum = ChecksumGenerator.generate(stored_file["file_path"])

            existing_dataset = (
                self.dataset_repository
                .get_by_checksum(checksum)
            )

            if existing_dataset:
                raise DuplicateDatasetException("Dataset already exists.")

            stored_file = FileStorage.save(file)

            metadata = DatasetParser.extract_metadata(stored_file["file_path"])

            dataset = Dataset(
                original_filename=file.filename,
                stored_filename=stored_file["stored_filename"],
                file_path=stored_file["file_path"],
                file_size_bytes=file.content_length,
                checksum=checksum,
                file_type=file_type,
                row_count=metadata["row_count"],
                column_count=metadata["column_count"],
                status=DatasetStatus.UPLOADED
            )

            saved_dataset = self.dataset_repository.create(dataset)
            saved_dataset.status = DatasetStatus.VALIDATING
            self.dataset_repository.update(saved_dataset)

            validation = self.dataset_validator.validate_dataset(
                saved_dataset,
                metadata
            )

            if validation.passed:
                saved_dataset.status = DatasetStatus.READY
            else:
                saved_dataset.status = DatasetStatus.FAILED

            self.dataset_repository.update(saved_dataset)

            return {
                "dataset_id": str(saved_dataset.id),
                "status": saved_dataset.status.value,
                "errors": validation.errors,
                "passed": validation.passed
            }
        
        except AppException:
            raise
        except Exception as e:
            print(e)
            raise AppException("Could not upload dataset.")

    def get_all_datasets(self):
        try:
            datasets = self.dataset_repository.get_all()

            return [
                self.serialize_summary(dataset)
                for dataset in datasets
            ]
        except Exception:
            raise AppException("Could not get datasets.")
    
    def get_dataset_by_id(self, dataset_id):
        try:
            dataset = self.dataset_repository.get_by_id(
                dataset_id
            )

            if dataset is None:
                return None

            return self.serialize_dataset(dataset)
        except Exception:
            raise AppException(f"Could not get dataset {dataset_id}.")


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
            "uploaded_at": dataset.uploaded_at.isoformat(),
            "version": dataset.version
        }

    def serialize_summary(self, dataset):

        return {
            "id": str(dataset.id),
            "original_filename": dataset.original_filename,
            "status": dataset.status.value,
            "row_count": dataset.row_count,
            "column_count": dataset.column_count,
            "uploaded_at": dataset.uploaded_at.isoformat()
        }