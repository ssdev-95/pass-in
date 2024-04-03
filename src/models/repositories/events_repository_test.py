from .events_repository import EventsRepository
from ..settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

skip = """
def test_insert_event():
    events_repository = EventsRepository()
    event = {
        'uuid': '29fjs-02kfsol-01djsno2-02mfd9k2pq-02ie',
        'title': 'Some Wonderfull Title',
        'slug': 'some-wonderfull-title',
        'maximum_attendees': 20
    }

    events_repository.insert_event(event)


def test_get_event_by_id():
    event_id = '29fjs-02kfsol-01djsno2-02mfd9k2pq-02ie'
    events_repository = EventsRepository()
    events_repository.get_event_by_id(event_id)
"""

print(skip)

def test_count_attendees_from_event():
    event_id = '29fjs-02kfsol-01djsno2-02mfd9k2pq-02ie'
    events_repository = EventsRepository()
    res = events_repository.count_attendees_from_event(event_id)
    print(res)

