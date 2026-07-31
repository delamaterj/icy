from flask import jsonify

from app.common.exceptions import (
    AppException,
    ValidationException
)


def register_error_handlers(app):

    @app.errorhandler(ValidationException)
    def handle_validation(error):
        return jsonify({
            "status": "FAILED",
            "errors": error.errors
        }), error.status_code


    @app.errorhandler(AppException)
    def handle_application(error):
        return jsonify({
            "status": "FAILED",
            "message": error.message
        }), error.status_code


    @app.errorhandler(Exception)
    def handle_unexpected(error):
        app.logger.exception(error)
        return jsonify({
            "status": "ERROR",
            "message": "Internal server error."
        }), 500