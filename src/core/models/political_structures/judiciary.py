from pydantic import BaseModel
from typing import List

class Judiciary(BaseModel):
 name: str
 judges: List[str]
 location: str
