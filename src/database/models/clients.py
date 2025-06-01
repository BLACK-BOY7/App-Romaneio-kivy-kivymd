from typing import Optional
from sqlmodel import SQLModel, Field

class Client(SQLModel, table=True):
    __tablename__: str = "Clients"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
