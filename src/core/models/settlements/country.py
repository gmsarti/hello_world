from pydantic import BaseModel
from typing import Optional

class Country(BaseModel):
   name: str
   population: int
   area: float
   capital: str
   currency: str
