from typing import Sequence

from sqlmodel import select
from sqlalchemy.exc import IntegrityError

# Custom Imports...
from ..database import SessionManager
from ..models.clients import Client

class ControlClient:
    
    @staticmethod
    def create_client(name: str):
        session = SessionManager.get_session()
        client = Client(name=name)
        try:
            session.add(client)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"Cliente com nome '{name}' já existe.")

    @staticmethod
    def get_client_by_id(id: int) -> Client | None:
        session = SessionManager.get_session()
        return session.get(Client, id)
    
    @staticmethod
    def get_client_by_name(name: str) -> Client | None:
        session = SessionManager.get_session()
        statement = select(Client).where(Client.name == name)
        return session.exec(statement).first()
    
    @staticmethod
    def get_all_clients(self) -> Sequence[Client]:
        session = SessionManager.get_session()
        statement = select(Client)
        return session.exec(statement).all()
    
    @staticmethod
    def get_clients_paginated(offset: int, limit: int) -> Sequence[Client]:
        session = SessionManager.get_session()
        statement = select(Client).offset(offset).limit(limit)
        return session.exec(statement).all()
    
    @staticmethod
    def update_client_name(client: Client, name: str):
        session = SessionManager.get_session()
        try:
            client.name = name
            session.add(client)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"Não foi possível atualizar. Nome '{name}' já existe.")

    @staticmethod
    def is_name_taken(name: str) -> bool:
        session = SessionManager.get_session()
        statement = select(Client).where(Client.name == name)
        result = session.exec(statement)
        return result.first() is not None