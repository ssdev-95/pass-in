from typing import Dict
from sqlalchemy.exc import IntegrityError, NoResultFound

from ..settings.connection import db_connection_handler
from ..entities.attendee import Attendee

class AttendeesRepository:
    def insert_attendee(self, attendee_info:Dict):
        with db_connection_handler as db:
            try:
                attendee = Attendee(
                    id=attendee_info.get('uuid'),
                    name=attendee_info.get('name'),
                    email=attendee_info.get('email'),
                    event_id=attendee_info.get('event_id')
                )

                db.session.add(attendee)
                db.session.commit()
                return attendee_info
            except IntegrityError:
                raise Exception('[ERROR] · Failed To Save Attendee')
            except Exception as err:
                db.session.rollback()
                raise err
    def get_attendees_by_event_id(self, event_id:str):
        with db_connection_handler as db:
            try:
                attendee = db.session.query(Attendee).filter(Attendee.event_id==event_id).all()
                return attendee
            except NoResultFound:
                raise Exception(f'[ERROR] · Attendee Not Found In Event <{event_id}>')
            except Exception as err:
                print(f'[ERROR] · {err}')
                raise err
