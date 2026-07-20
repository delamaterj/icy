from flask import Flask
from app.config.settings import Config
from app.extensions import cors, db
from app.routes.health_routes import health_bp


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(Config)

    cors.init_app(app)

    app.register_blueprint(health_bp)

    db.init_app(app)

    return app