from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ...config import CONFIG

class __DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = '{}:///{}'.format(
            CONFIG['DB_DIALECT'],
            CONFIG['DB_URL']
        )
        self.__engine = None
        #self.session = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.session.close()


db_connection_handler = __DbConnectionHandler()
