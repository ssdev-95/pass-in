from uuid import uuid4

from src.http_types.http_request import HTTPRequest
from src.http_types.http_response import HTTPResponse
from src.models.repositories.events_repository import EventsRepository
from src.models.repositories.attendees_repository import AttendeesRepository

class EventsHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()
        self.__attendees_repository = AttendeesRepository()

    def create_event(self, http_request:HTTPRequest)->HTTPResponse:
        event_info = http_request.body
        event_info['uuid'] = str(uuid4())

        event = self.__events_repository.insert_event(event_info)

        return HTTPResponse(
            body={ 'eventId': event.get('uuid') },
            status_code=201
        )
    
    def find_by_id(self, http_request:HTTPRequest)->HTTPResponse:
        event_id = str(http_request.params.get('event_id'))
        event = self.__events_repository.get_event_by_id(event_id)

        if event is None:
            raise Exception('[ERROR] · Event Not Found')

        attendees_count = self.__events_repository.count_attendees_from_event(event_id)

        return HTTPResponse(body={
            'event': {
                'id': event.id,
                'title': event.title,
                'details': event.details,
                'slug': event.slug,
                'maximumAttendees': event.maximum_attendees,
                'attendeesAmount': attendees_count.get('attendeesAmount')
            }
        })

    def get_attendees_from_event(self, http_request:HTTPRequest)->HTTPResponse:
        event_id = str(http_request.params.get('event_id'))
        attendees = self.__attendees_repository.get_attendees_by_event_id(event_id)

        return HTTPResponse(
            body={ 'attendees': attendees }
        )
