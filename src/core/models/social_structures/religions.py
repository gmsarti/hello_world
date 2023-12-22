from pydantic import BaseModel
from typing import List

class Religion(BaseModel):
 name: str
 beliefs: List[str]
 practitioners: int
