from flask import Blueprint, request

from src.data.events_handler import EventsHandler
from src.data.attendees_handler import AttendeesHandler
from src.http_types.http_request import HTTPRequest

from src.exceptions.exceptions_handler import exceptions_handler

blueprint = Blueprint('events_routes', __name__)

@blueprint.route('/events', methods=['POST'])
def insert_event():
    try:
        events_handler = EventsHandler()
        http_request = HTTPRequest(body=request.json)
        http_response = events_handler.create_event(http_request)
        return http_response.__json__(), http_response.status_code
    except Exception as err:
        http_response = exceptions_handler(err)
        return http_response.__json__(), http_response.status_code


@blueprint.route('/events/<event_id>', methods=['GET'])
def get_event_info(event_id:str):
    try:
        events_handler = EventsHandler()
        http_request = HTTPRequest(params={
            'event_id': event_id
        })
        http_response = events_handler.find_by_id(http_request)
        return http_response.__json__(), http_response.status_code
    except Exception as err:
        http_response = exceptions_handler(err)
        return http_response.__json__(), http_response.status_code

@blueprint.route('/events/<event_id>/attendees', methods=['GET'])
def get_attendees_from_event(event_id:str):
    try:
        events_handler = EventsHandler()
        http_request = HTTPRequest(params={
            'event_id': event_id
        })

        http_response = events_handler.get_attendees_from_event(http_request)
        return http_response.__json__(), http_response.status_code
    except Exception as err:
        http_response = exceptions_handler(err)
        return http_response.__json__(), http_response.status_code

@blueprint.route('/events/<event_id>/register', methods=['POST'])
def join_an_event(event_id:str):
    try:
        attendees_handler = AttendeesHandler()
        http_request = HTTPRequest(
            body=request.form,
            params={ 'event_id': event_id }
        )
        http_response = attendees_handler.register_attendee(http_request)
        return http_response.__json__(), http_response.status_code
    except Exception as err:
        http_response = exceptions_handler(err)
        return http_response.__json__(), http_response.status_code

