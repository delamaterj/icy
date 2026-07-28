class AppException(Exception):
    status_code = 500
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ValidationException(AppException):
    status_code = 400
    def __init__(self, errors: list[str]):
        self.errors = errors
        super().__init__("Dataset validation failed.")


class DatabaseException(AppException):
    status_code = 500


class DuplicateDatasetException(AppException):
    status_code = 409
    def __init__(self):
        super().__init__("Duplicate dataset detected.")


class ResourceNotFoundException(AppException):
    status_code = 404


class StorageException(AppException):
    status_code = 500