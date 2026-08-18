from flask import Flask
from app.config.settings import Config
from app.extensions import cors, db
from app.modules.health.routes.health_routes import health_bp
from app.modules.datasets.routes.dataset_routes import dataset_bp
from app.modules.experiments.routes.experiment_routes import experiment_bp
from app.modules.training_runs.routes.training_run_routes import training_run_bp
from app.common.error_handlers import register_error_handlers

def create_app() -> Flask:
    
    app = Flask(__name__)
    app.config.from_object(Config)
    cors.init_app(app)
    app.register_blueprint(health_bp)
    app.register_blueprint(dataset_bp)
    app.register_blueprint(experiment_bp)
    app.register_blueprint(training_run_bp)
    db.init_app(app)
    register_error_handlers(app)

    return app