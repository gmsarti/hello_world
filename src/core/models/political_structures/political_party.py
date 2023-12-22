from pydantic import BaseModel
from typing import List

class PoliticalParty(BaseModel):
 name: str
 ideology: str
 leaders: List[str]
