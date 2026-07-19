from flask import Flask

from app.extensions import cors
from app.routes.health_routes import health_bp


def create_app() -> Flask:
    app = Flask(__name__)

    cors.init_app(app)

    app.register_blueprint(health_bp)

    return app