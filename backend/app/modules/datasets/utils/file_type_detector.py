import os

from app.enums.file_type import FileType
from app.common.exceptions import ValidationException


class FileTypeDetector:

    EXTENSION_MAP = {
        ".csv": FileType.CSV,
        ".json": FileType.JSON,
        ".parquet": FileType.PARQUET,
    }

    @staticmethod
    def detect(filename: str) -> FileType:

        extension = os.path.splitext(filename)[1].lower()

        if extension not in FileTypeDetector.EXTENSION_MAP:
            raise ValidationException(
                f"Unsupported file extension: {extension}"
            )

        return FileTypeDetector.EXTENSION_MAP[extension]