from sqlmodel import SQLModel

# custom imports... load models...
from .session import SessionManager
from .models import Client, Order, OrderPage


class DataBase:
    @staticmethod
    def init_data_base():
        SQLModel.metadata.create_all(SessionManager.get_engine())