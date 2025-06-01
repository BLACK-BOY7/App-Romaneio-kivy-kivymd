import os

from sqlmodel import Session, create_engine

class SessionManager:
    _engine = None
    _session = None
    _file_name = None

    @classmethod
    def get_file_name(cls):
        if cls._file_name is None:
            cls._file_name = f"sqlite:///{os.path.join(os.getcwd(), "src/database/romaneios.db")}"
        return cls._file_name

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            cls._engine = create_engine(cls.get_file_name())
        return cls._engine

    @classmethod
    def get_session(cls):
        if cls._session is None:
            cls._session = Session(cls.get_engine())
        return cls._session

    @classmethod
    def close_session(cls):
        if cls._session:
            cls._session.close()
            cls._session = None