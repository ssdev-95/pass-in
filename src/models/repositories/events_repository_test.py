from .events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler

from init.test_mocks import mock_event

db_connection_handler.connect_to_db()

def test_insert_event():
    events_repository = EventsRepository()
    event = mock_event
    events_repository.insert_event(event)


def test_get_event_by_id():
    event_id = mock_event['uuid']
    events_repository = EventsRepository()
    events_repository.get_event_by_id(event_id)


def test_count_attendees_from_event():
    event_id = mock_event['uuid']
    events_repository = EventsRepository()
    events_repository.count_attendees_from_event(event_id)
