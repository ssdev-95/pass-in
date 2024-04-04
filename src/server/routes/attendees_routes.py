from flask import Blueprint, request, make_response

from src.data.attendees_handler import AttendeesHandler
from src.http_types.http_request import HTTPRequest

attendees_routes_bp = Blueprint('attendees_routes', __name__)

@attendees_routes_bp.route('/attendees/<attendee_id>/check_in', methods=['POST'])
def check_in(attendee_id:int):
    attendees_handler = AttendeesHandler()
    http_request = HTTPRequest(
        body=request.json,
        params={
            'attendee_id': attendee_id
        }
    )

    http_response = attendees_handler.handle_check_in(http_request)
    print(http_request.body)
    return make_response(), http_response.status_code


@attendees_routes_bp.route('/attendees/<attendee_id>/badge', methods=['GET'])
def get_event_attendee_badge(attendee_id:int):
    attendees_handler = AttendeesHandler()
    http_request = HTTPRequest(
        params={ 'attendee_id': attendee_id }
    )

    http_response = attendees_handler.get_attendee_badge(http_request)
    return http_response.body, http_response.status_code
