from flask import jsonify

from app.modules.health.services.health_services import HealthService

health_service = HealthService()


def get_health():
    response = health_service.get_health()

    return jsonify(response), 200