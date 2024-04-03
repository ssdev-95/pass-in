from flask import Flask
from flask_cors import CORS

from .routes.events_routes import events_routes_bp
from src.models.settings.connection import db_connection_handler

def create_app():
    db_connection_handler.connect_to_db()

    flask_app = Flask(__name__)
    CORS(flask_app)

    flask_app.register_blueprint(events_routes_bp)

    return flask_app
