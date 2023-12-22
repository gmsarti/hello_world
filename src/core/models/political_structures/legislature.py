from pydantic import BaseModel
from typing import List

class Legislature(BaseModel):
 name: str
 members: List[str]
 location: str
