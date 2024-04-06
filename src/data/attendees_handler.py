from datetime import datetime
from uuid import uuid4
from src.exceptions.exception_types.http_not_found import HTTPNotFoundException

from src.http_types.http_request import HTTPRequest
from src.http_types.http_response import HTTPResponse
from src.exceptions.exception_types.http_conflict import HTTPConflictException
from src.models.repositories.attendees_repository import AttendeesRepository
from src.models.repositories.check_in_repository import CheckInRepository
from src.models.repositories.events_repository import EventsRepository

class AttendeesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__check_in_repository = CheckInRepository()
        self.__events_repository = EventsRepository()

    def register_attendee(self, http_request:HTTPRequest) -> HTTPResponse:
        event_id = str(http_request.params.get('event_id'))
        event = self.__events_repository.get_event_by_id(event_id)
        if not event:
            raise HTTPNotFoundException(message='Cannot Attend Non Existent Event')

        event_end = datetime.fromisoformat(str(event.end_date))
        if event_end < datetime.now():
            raise HTTPConflictException(message='Cannot Receive Attendees After Event Ends')

        attendee_info = http_request.body
        attendee_info['event_id'] = event_id
        attendee_info['uuid'] = str(uuid4())
        attendee = self.__attendees_repository.insert_attendee(attendee_info)

        attendees_count = self.__events_repository.count_attendees_from_event(attendee_info['event_id'])

        can_have_attendees = attendees_count['maximumAttendees']>0
        event_is_full_capacity = attendees_count['maximumAttendees'] == attendees_count['attendeesAmount']

        if can_have_attendees and event_is_full_capacity:
            raise HTTPConflictException(message='Event Is At Full Capacity')

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

    def handle_check_in(self, http_request:HTTPRequest) -> HTTPResponse:
        attendee_id = str(http_request.params.get('attendee_id'))
        self.__check_in_repository.handle_check_in(attendee_id)
        return HTTPResponse(body={}, status_code=201)
