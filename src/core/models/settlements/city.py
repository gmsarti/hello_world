from pydantic import BaseModel
from typing import Optional

class City(BaseModel):
   name: str
   population: int
   area: float
   currency: str
   language: str
