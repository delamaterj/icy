from enum import Enum


class FileType(str, Enum):
    """
    Supported dataset file formats.
    """

    CSV = "CSV"
    PARQUET = "PARQUET"
    JSON = "JSON"