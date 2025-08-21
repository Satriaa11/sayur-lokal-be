from flask import Flask
from flask_cors import CORS
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig
from app.utils.extensions import db, migrate
from app.models import *  # noqa: F401,F403
from app.routes.auth_routes import auth_bp
from app.routes.user_routes import user_bp
from app.routes.product_routes import product_bp
from app.routes.category_routes import category_bp
from app.routes.order_routes import order_bp
from app.routes.rating_routes import rating_bp
from app.routes.test_routes import test_bp

# from app.routes.dashboard_routes import dashboard_bp


def create_app(config_class=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize CORS
    CORS(app, 
         origins=app.config.get('CORS_ORIGINS', ["*"]),
         methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
         allow_headers=[
             "Content-Type",
             "Authorization",
             "Access-Control-Allow-Credentials",
             "X-Requested-With",
             "Accept",
             "Origin"
         ],
         supports_credentials=True,
         max_age=3600
    )

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(rating_bp)
    app.register_blueprint(test_bp)
    # app.register_blueprint(dashboard_bp)

    return app
