from flask import Blueprint, request

from src.data.events_handler import EventsHandler
from src.http_types.http_request import HTTPRequest

events_routes_bp = Blueprint('events_routes', __name__)

@events_routes_bp.route('/events', methods=['POST'])
def insert_event():
    events_handler = EventsHandler()
    http_request = HTTPRequest(body=request.json)
    http_response = events_handler.create_event(http_request)
    return http_response.__json__(), http_response.status_code


@events_routes_bp.route('/events/<event_id>', methods=['GET'])
def get_event_badge(event_id:str):
    events_handler = EventsHandler()
    http_request = HTTPRequest(params={
        'event_id': event_id
    })
    http_response = events_handler.find_by_id(http_request)
    return http_response.__json__(), http_response.status_code

@events_routes_bp.route('/events/<event_id>/attendees', methods=['GET'])
def get_attendees_from_event(event_id:str):
    events_handler = EventsHandler()
    http_request = HTTPRequest(params={
        'event_id': event_id
    })

    http_response = events_handler.get_attendees_from_event(http_request)
    return http_response.__json__(), http_response.status_code

