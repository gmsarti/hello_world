from pydantic import BaseModel
from typing import List

class Family(BaseModel):
 name: str
 members: List[str]
 address: str
