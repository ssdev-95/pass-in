from src.http_types.http_request import HTTPRequest

from .events_handler import EventsHandler
from .attendees_handler import AttendeesHandler

from init.test_mocks import create_attendee_mock, create_event_mock
from src.models.settings.connection import db_connection_handler


db_connection_handler.connect_to_db()
attendees_handler = AttendeesHandler()
events_handler = EventsHandler()

mock_event = create_event_mock()
mock_attendee = create_attendee_mock(event_id=mock_event['uuid'])


mock_http_request = HTTPRequest(
    body=mock_attendee,
    params={
        'event_id': mock_event['uuid'],
        'attendee_id': mock_attendee['uuid']
    }
)

def test_register_attendee():
    attendees_handler.register_attendee(mock_http_request)


def test_get_attendee_badge():
    attendees_handler.get_attendee_badge(mock_http_request)


def test_handle_check_in():
    attendees_handler.handle_check_in(mock_http_request)

