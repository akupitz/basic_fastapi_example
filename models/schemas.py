from pydantic import BaseModel
from typing import Optional, List


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


class Product(BaseModel):
    name: str
    amount: int
    price: float

