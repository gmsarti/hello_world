from pydantic import BaseModel
from typing import List

class GovernmentType(BaseModel):
 name: str
 characteristics: List[str]
 countries: List[str]
