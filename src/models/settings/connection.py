from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ...config import CONFIG

class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = '{}:///{}'.format(
            CONFIG['DB_DIALECT'],
            CONFIG['DB_URL']
        )
        self.__engine = None
        self.__session = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.__session = session_maker(bind=self.__engine)
        return self

    def __exit__(self):
        if self.__session is None:
            return
        self.__session.close()
