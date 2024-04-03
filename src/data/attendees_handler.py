from uuid import uuid4

from src.http_types.http_request import HTTPRequest
from src.http_types.http_response import HTTPResponse
from src.models.repositories.attendees_repository import AttendeesRepository


class AttendeesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()

    def register_attendee(self, http_request:HTTPRequest) -> HTTPResponse:
        attendee_info = http_request.body
        attendee_info['uuid'] = str(uuid4())
        attendee_info['event_id'] = str(http_request.params.get('event_id'))

        attendee = self.__attendees_repository.insert_attendee(attendee_info)

        return HTTPResponse(
            body={ 'attendeeId': attendee.get('uuid') },
            status_code=201
        )

    def get_attendee_badge(self, http_request:HTTPRequest) -> HTTPResponse:
        attendee_id = str(http_request.params.get('attendee_id'))
        badge = self.__attendees_repository.get_attendee_badge_by_id(attendee_id)
        return HTTPResponse(
            body={ 'badge': badge }
        )
