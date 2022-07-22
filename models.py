from pydantic import BaseModel
from typing import List, Union


class Body(BaseModel):
    currencies: List[str]


class Currency(BaseModel):
    code: int
    name: str
    price: float
    time: str
    nominal: int


class Data(BaseModel):
    data: str
