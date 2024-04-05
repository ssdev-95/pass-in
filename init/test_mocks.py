# Mocks For Tests

mock_event_uuid =    '29fjs-02kfsol-01djsno2-02mfd9k2pq-02ie'
mock_attendee_uuid = '2wkci-1idjkdk-kwdn1mdo-kefjskksdk-92jn'

def create_event_mock(index=0):                                     return {
        'uuid': f'{mock_event_uuid}{index}',
        'title': f'Some Wonderfull Title {index}',
        'slug': f'some-wonderfull-title-{index}',
        'details': 'It\'s such a perfect day',
        'maximum_attendees': 20,
        'start_date': '2030-12-31T19:00:00',
        'end_date': '2031-01-10T19:00:00'
    }


def create_attendee_mock(event_id=f'{mock_event_uuid}0', index=0):
    return {
        'uuid': f'{mock_attendee_uuid}{index}',
        'name': f'John Doe {index}',
        'email': f'some-wonderfull-email-{index}.com',
        'event_id': event_id
    }


def create_bulk_event_mocks(quantity=10):
    mocks = []
    for mock in range(quantity):
        mocks.append(create_event_mock(mock))
    return mocks


def create_bulk_attendees_mocks(event_id, quantity=10):
    mocks = []
    for mock in range(quantity):
        mocks.append(create_attendee_mock(event_id, mock))
    return mocks

mock_event = create_event_mock()
mock_attendee = create_attendee_mock()
