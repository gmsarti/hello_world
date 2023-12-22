from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
  name: str
  age: int
  gender: str
  nationality: str
