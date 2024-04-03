from uuid import uuid4

from src.http_types.http_request import HTTPRequest
from src.http_types.http_response import HTTPResponse
from src.models.repositories.events_repository import EventsRepository

class EventsHandler:
    def __init__(self) -> None:
        self.__repository = EventsRepository()

    def create_event(self, http_request:HTTPRequest)->HTTPResponse:
        event_info = http_request.body
        event_info['uuid'] = str(uuid4())

        event = self.__repository.insert_event(event_info)

        return HTTPResponse(
            body={ 'eventId': event.get('uuid') },
            status_code=201
        )
    
    def find_by_id(self, http_request:HTTPRequest)->HTTPResponse:
        event_id = str(http_request.params.get('event_id'))
        event = self.__repository.get_event_by_id(event_id)

        if event is None:
            raise Exception('[ERROR] · Event Not Found')

        return HTTPResponse(body={
            'event': {
                'id': event.id,
                'title': event.title,
                'details': event.details,
                'slug': event.slug,
                'maximumAttendees': event.maximum_attendees,
                'attendeesAmount': 0
            }
        })
