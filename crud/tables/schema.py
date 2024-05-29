from pydantic import BaseModel

class user(BaseModel):
      id : int
      name : str
      category : str
      price : float
      