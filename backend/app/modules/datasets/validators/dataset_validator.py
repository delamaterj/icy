import os
from app.modules.datasets.validators.validation_result import ValidationResult


class DatasetValidator:

    REQUIRED_COLUMNS = {
        "Label"
    }

    def _validate_file_exists(
        self,
        file_path: str,
        result: ValidationResult
    ):
        if not os.path.exists(file_path):
            result.add_error("Dataset file does not exist")

    def _validate_not_empty(
        self,
        metadata: dict,
        result: ValidationResult
    ):

        if metadata["row_count"] <= 0:
            result.add_error("Dataset contains no rows")

        if metadata["column_count"] <= 0:
            result.add_error("Dataset contains no columns")

    def _validate_required_columns(
        self,
        metadata: dict,
        result: ValidationResult
    ):

        columns = set(metadata["columns"])
        missing = self.REQUIRED_COLUMNS - columns

        if missing:
            result.add_error(
                "Missing required columns: "
                + ", ".join(sorted(missing))
            )

    def validate_dataset(
        self,
        dataset,
        metadata: dict
    ) -> ValidationResult:

        result = ValidationResult()

        self._validate_file_exists(dataset.file_path, result)
        self._validate_not_empty(metadata, result)
        self._validate_required_columns(metadata, result)

        return result