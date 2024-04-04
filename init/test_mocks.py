# Mocks For Tests

mock_event_uuid =    '29fjs-02kfsol-01djsno2-02mfd9k2pq-02ie'
mock_attendee_uuid = '2wkci-1idjkdk-kwdn1mdo-kefjskksdk-92jn'

mock_event = {
    'uuid': mock_event_uuid,
    'title': 'Some Wonderfull Title',
    'slug': 'some-wonderfull-title',
    'details': 'It\'s such a perfect day',
    'maximum_attendees': 20
}

mock_attendee = {
    'uuid': mock_attendee_uuid,
    'name': 'John Dpe',
    'email': 'some-wonderfull-email.com',
    'event_id': mock_event_uuid
}
