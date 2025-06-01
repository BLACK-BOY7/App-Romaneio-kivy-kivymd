from typing import List

from sqlmodel import select
from sqlalchemy.orm import selectinload

# Custom Imports...
from ..models.orders import Order, OrderPage
from ..database import SessionManager

class ControlOrder:

    @staticmethod
    def create_order(wood_type: str, creatin_date: str, client_id: int, observation: str = ""):
        session = SessionManager.get_session()
        order = Order(
            wood_type=wood_type,
            creatin_date=creatin_date,
            client_id=client_id,
            observation=observation
        )
        session.add(order)
        session.commit()

    @staticmethod
    def get_all_orders() -> List[Order]:
        session = SessionManager.get_session()
        statement = select(Order)
        return session.exec(statement).all()

    @staticmethod
    def get_all_orders_by_client_id(client_id: int) -> List[Order]:
        session = SessionManager.get_session()
        statement = select(Order).where(Order.client_id == client_id)
        return session.exec(statement).all()

    @staticmethod
    def get_first_order_by_client_id(client_id: int) -> Order | None:
        session = SessionManager.get_session()
        statement = select(Order).where(Order.client_id == client_id)
        return session.exec(statement).first()

    @staticmethod
    def get_orders_paginated(offset: int, limit: int) -> List[Order]:
        session = SessionManager.get_session()
        statement = select(Order).offset(offset).limit(limit)
        return session.exec(statement).all()

    @staticmethod
    def get_orders_by_client_paginated(client_id: int, offset: int, limit: int) -> List[Order]:
        session = SessionManager.get_session()
        statement = (
            select(Order)
            .where(Order.client_id == client_id)
            .offset(offset)
            .limit(limit)
        )
        return session.exec(statement).all()
    
    @staticmethod
    def create_order_page(page_number: int,  order_id: int, height: float = None, width: float = None, amount: int = None):
        session = SessionManager.get_session()

        order_page = OrderPage(
            page_number=page_number,
            height=height,
            width=width,
            amount=amount,
            order_id=order_id,
        )
        session.add(order_page)
        session.commit()

    @staticmethod
    def get_all_order_pages_by_id(order_id) -> Order:
        session = SessionManager.get_session()
        statement = (
            select(Order)
            .where(Order.id == order_id)
            .options(selectinload(Order.pages))  # eager load das páginas
        )

        return session.exec(statement).first()