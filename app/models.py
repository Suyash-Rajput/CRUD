from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Item(Base):
    __tablename__ = "product_details"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    category = Column(String(255), index=True)
    price = Column(Float, index=True)
