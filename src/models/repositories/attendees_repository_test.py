from .attendees_repository import AttendeesRepository
from ..settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

def test_insert_attendee():
    attendees_repository = AttendeesRepository()
    attendee = {
        'uuid': '2wkciw-wjg83n3-kw9xkeeife3-wjf8k2e8cjaUWJDj',
        'name': 'John Dpe',
        'email': 'some-wonderfull-email.com',
        'event_id': '29fjs-02kfsol-01djsno2-02mfd9k2pq-02ie',
    }

    attendees_repository.insert_attendee(attendee)


def test_get_attendees_by_event_id():
    event_id = '29fjs-02kfsol-01djsno2-02mfd9k2pq-02ie'
    attendees_repository = AttendeesRepository()
    attendees_repository.get_attendees_by_event_id(event_id)
