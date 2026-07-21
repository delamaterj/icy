from flask import Flask
from app.config.settings import Config
from app.extensions import cors, db
from app.modules.health.routes.health_routes import health_bp
from app.modules.datasets.routes.dataset_routes import dataset_bp


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(Config)

    cors.init_app(app)

    app.register_blueprint(health_bp)

    app.register_blueprint(dataset_bp)

    db.init_app(app)

    return app