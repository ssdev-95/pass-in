from typing import Dict
from sqlalchemy.exc import IntegrityError

from ..settings.connection import db_connection_handler
from ..entities.event import Event

class EventsRepository:
    def insert_event(self, event_info:Dict):
        with db_connection_handler as db:
            try:
                event = Event(
                    id=event_info.get('uuid'),
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
            return db.session.query(Event).filter(Event.id==event_id).one_or_none()
