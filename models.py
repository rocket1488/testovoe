from pydantic import BaseModel
from typing import List


class Body(BaseModel):
    currencies: List[str]
