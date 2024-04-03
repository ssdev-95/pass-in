from ..settings.connection import db_connection_handler
from ..entities.check_in import CheckIn

class CheckInRepository:
    def handle_check_in(self, attendee_id:str)->CheckIn:
        with db_connection_handler as db:
            try:
                check_in  = CheckIn(
                    attendee_id = attendee_id
                )

                db.session.add(check_in)
                db.session.commit()
                return check_in
            except IntegrityError:
                raise Exception('[ERROR] · Failed To CheckIn In Event')
            except Exception as err:
                db.session.rollback()
                raise err
