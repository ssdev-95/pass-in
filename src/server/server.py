from flask import Flask
from flask_cors import CORS

from .routes import events_routes, attendees_routes, swagger_ui
from src.models.settings.connection import db_connection_handler

blueprints = [
    attendees_routes.blueprint,
    events_routes.blueprint,
    swagger_ui.blueprint
]

def create_app():
    db_connection_handler.connect_to_db()

    flask_app = Flask(__name__)
    CORS(flask_app)

    for blueprint in blueprints:
        flask_app.register_blueprint(blueprint)

    return flask_app
