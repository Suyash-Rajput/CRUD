from pydantic import BaseModel

class ItemBase(BaseModel):
    id : int
    name: str
    category: str
    price: float

class ItemBaseItem(BaseModel):
     name: str
     category: str
     price: float

class ItemUpdate(ItemBaseItem):
     pass

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
