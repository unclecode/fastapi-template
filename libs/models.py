# models.py
from pydantic import BaseModel

class Item(BaseModel):
    user_id: str
    description: str
    price: float

class Login(BaseModel):
    user_id: str
    email: str