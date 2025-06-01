from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

__all__ = "Order", "OrderPage"

class Order(SQLModel, table=True):
    __tablename__: str = "Orders"

    id: Optional[int] = Field(default=None, primary_key=True)
    wood_type: str
    creatin_date: str
    observation: Optional[str] = Field(default="")
    
    client_id: int = Field(foreign_key="Clients.id")

    pages: List["OrderPage"] = Relationship(back_populates="order")


class OrderPage(SQLModel, table=True):
    __tablename__: str = "OrderPages"

    id: Optional[int] = Field(default=None, primary_key=True)
    page_number: int
    order_id: int = Field(foreign_key="Orders.id")

    # ---------- start - bitolas ---------- #
    height: Optional[float] = Field(default=None)
    width: Optional[float] = Field(default=None)
    amount: Optional[int] = Field(default=None)
    # ---------- end ---------- #

    # ---------- start - comprimentos ---------- #
    cm_250: Optional[int] = Field(default=0)
    cm_300: Optional[int] = Field(default=0)
    cm_350: Optional[int] = Field(default=0)
    cm_400: Optional[int] = Field(default=0)
    cm_450: Optional[int] = Field(default=0)
    cm_500: Optional[int] = Field(default=0)
    cm_550: Optional[int] = Field(default=0)
    cm_600: Optional[int] = Field(default=0)
    cm_650: Optional[int] = Field(default=0)
    cm_700: Optional[int] = Field(default=0)
    cm_750: Optional[int] = Field(default=0)
    cm_800: Optional[int] = Field(default=0)
    cm_850: Optional[int] = Field(default=0)
    cm_900: Optional[int] = Field(default=0)
    cm_950: Optional[int] = Field(default=0)
    cm_1000: Optional[int] = Field(default=0)
    # ---------- end ---------- #

    order: Optional["Order"] = Relationship(back_populates="pages")