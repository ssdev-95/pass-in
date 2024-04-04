from typing import Dict
from uuid import uuid4
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError, NoResultFound

from src.models.settings.connection import db_connection_handler
from src.models.entities.event import Event
from src.models.entities.attendee import Attendee

class EventsRepository:
    def insert_event(self, event_info:Dict):
        with db_connection_handler as db:
            try:
                event = Event(
                    id=str(uuid4()),
                    title=event_info.get('title'),
                    details=event_info.get('details'),
                    slug=event_info.get('slug'),
                    maximum_attendees=event_info.get('maximum_attendees')
                )

                db.session.add(event)
                db.session.commit()
                return event_info
            except IntegrityError:
                raise Exception('[ERROR] · Failed To Save Event')
            except Exception as err:
                db.session.rollback()
                raise err

    def get_event_by_id(self, event_id:str):
        with db_connection_handler as db:
            try:
                event = db.session.query(Event).filter(Event.id==event_id).one()
                return event
            except NoResultFound:
                raise Exception(f'[ERROR] · Event Not Found <{event_id}>')
            except Exception as err:
                print(f'[ERROR] · {err}')
                raise err

    def count_attendees_from_event(self, event_id:str):
        with db_connection_handler as db:
            try:
                attendee = (
                    db.session.query(Event)
                        .join(Attendee, Attendee.event_id==event_id)
                        .filter(Event.id==event_id)
                        .with_entities(
                            Event.maximum_attendees.label('maximumAttendees'),
                            func.count(Attendee.id).label('attendeesAmount')
                        ).one()
                )

                return {
                    'maximumAttendees': attendee[0],
                    'attendeesAmount': attendee[1]
                }
            except Exception as err:
                print(err)
                return {
                    'maximumAttendees': 0,
                    'attendeesAmount': 0
                }
