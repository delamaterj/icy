import os

from app.enums.file_type import FileType
from app.common.exceptions import AppException


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
            return None

        return FileTypeDetector.EXTENSION_MAP[extension]