from flask import Blueprint

from app.controllers.health_controllers import get_health

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    return get_health()