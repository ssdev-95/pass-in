from sqlalchemy.exc import IntegrityError



from src.exceptions.exception_types.http_bad_request import HTTPBadRequestException
from src.exceptions.exception_types.http_conflict import HTTPConflictException

from src.models.settings.connection import db_connection_handler
from src.models.entities.check_in import CheckIn

class CheckInRepository:
    def handle_check_in(self, attendee_id:str)->CheckIn:
        with db_connection_handler as db:
            try:
                check_in = CheckIn(
                    attendee_id = attendee_id
                )

                db.session.add(check_in)
                db.session.commit()
                return check_in
            except IntegrityError:
                raise HTTPConflictException('[ERROR] · Failed To CheckIn In Event')
            except Exception as err:
                db.session.rollback()
                raise HTTPBadRequestException(f'{err}')
