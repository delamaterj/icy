import hashlib
from app.common.exceptions import AppException


class ChecksumGenerator:

    @staticmethod
    def generate(file_path):
        try:
            sha256 = hashlib.sha256()

            with open(file_path, "rb") as file:

                while chunk := file.read(4096):
                    sha256.update(chunk)

            return sha256.hexdigest()
        except IOError:
            raise AppException("Unable to generate checksum.")