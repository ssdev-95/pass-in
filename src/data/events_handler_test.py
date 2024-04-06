from src.http_types.http_request import HTTPRequest
from .events_handler import EventsHandler
from .attendees_handler import AttendeesHandler
from init.test_mocks import create_bulk_attendees_mocks, create_event_mock
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()
events_handler = EventsHandler()

mock_event = create_event_mock()
attendees_mocks = create_bulk_attendees_mocks(event_id=mock_event['uuid'], quantity=3)

event_id = ''

def test_create_event():
    http_request = HTTPRequest(body=mock_event)
    http_response = events_handler.create_event(http_request)

    global event_id
    event_id = http_response.body.get('eventId')
    print(event_id)


def test_find_by_id():
    print(event_id)
    http_request = HTTPRequest(params={'event_id':event_id})
    events_handler.find_by_id(http_request)


def test_get_attendees_from_event():
    print(event_id)
    attendees_handler = AttendeesHandler()

    for attendee in attendees_mocks:
        http_request = HTTPRequest(
            body=attendee,
            params={'event_id':event_id}
        )
        attendees_handler.register_attendee(http_request)

    events_handler.get_attendees_from_event(
        HTTPRequest(params={'event_id': event_id})
    )
