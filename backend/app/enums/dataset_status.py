from enum import Enum

class DatasetStatus(str, Enum):
    UPLOADED = "UPLOADED"
    VALIDATING = "VALIDATING"
    READY = "READY"
    FAILED = "FAILED"
    ARCHIVED = "ARCHIVED"