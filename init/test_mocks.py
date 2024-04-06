# Mocks For Tests
import re
from faker import Faker

fake = Faker()

def fake_slug(event_title):
    return re.sub('[^A-Z]', '', event_title, 0, re.IGNORECASE)

def create_event_mock():
    return {
        'uuid': fake.uuid4(),
        'title': fake.job(),
        'details': fake.text(),
        'maximum_attendees': 999,
        'start_date': '2030-12-31T19:00:00',
        'end_date': '2031-01-10T19:00:00'
    }


def create_attendee_mock(event_id):
    return {
        'uuid': fake.uuid4(),
        'name': fake.name(),
        'email': fake.email(),
        'event_id': event_id
    }


def create_bulk_event_mocks(quantity=10):
    mocks = []
    for _ in range(quantity):
        mocks.append(create_event_mock())
    return mocks


def create_bulk_attendees_mocks(event_id, quantity=10):
    mocks = []
    for _ in range(quantity):
        mocks.append(create_attendee_mock(event_id))
    return mocks

mock_event = create_event_mock()
mock_event['slug'] = fake_slug(mock_event.get('title'))
mock_event_uuid = mock_event.get('uuid')
mock_attendee = create_attendee_mock(mock_event.get('uuid'))
mock_attendee_uuid = mock_attendee.get('uuid')
