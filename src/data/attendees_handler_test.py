from src.http_types.http_request import HTTPRequest

from .events_handler import EventsHandler
from .attendees_handler import AttendeesHandler

from init.test_mocks import create_attendee_mock, create_event_mock
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()
attendees_handler = AttendeesHandler()
events_handler = EventsHandler()

mock_event = create_event_mock()

mock_event_id = events_handler.create_event(
    HTTPRequest(body=mock_event)
).body.get('eventId')

mock_attendee = create_attendee_mock(event_id=mock_event_id)
mock_attendee_id = ''

def test_register_attendee():
    http_request = HTTPRequest(
        body=mock_attendee,
        params={
            'event_id': mock_event_id
        }
    )
    global mock_attendee_id
    mock_attendee_id = attendees_handler.register_attendee(http_request).body.get('attendeeId')


def test_get_attendee_badge():
    http_request = HTTPRequest(
        params={
            'attendee_id': mock_attendee_id
        }
    )
    attendees_handler.get_attendee_badge(http_request)


def test_handle_check_in():
    http_request = HTTPRequest(
        params={
            'attendee_id': mock_attendee_id
        }
    )
    attendees_handler.handle_check_in(http_request)

