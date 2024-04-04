from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

from init.test_mocks import mock_attendee, mock_event_uuid

db_connection_handler.connect_to_db()

def test_insert_attendee():
    attendees_repository = AttendeesRepository()
    attendee = mock_attendee
    attendees_repository.insert_attendee(attendee)


def test_get_attendees_by_event_id():
    event_id = mock_event_uuid
    attendees_repository = AttendeesRepository()
    attendees = attendees_repository.get_attendees_by_event_id(event_id)
    print(attendees)
