from enum import Enum


class DatasetStatus(str, Enum):
    """
    Represents the current lifecycle state of a dataset.
    """

    UPLOADED = "UPLOADED"
    VALIDATING = "VALIDATING"
    READY = "READY"
    FAILED = "FAILED"
    ARCHIVED = "ARCHIVED"