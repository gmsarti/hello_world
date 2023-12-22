from pydantic import BaseModel
from typing import List

class Profession(BaseModel):
 title: str
 description: str
 qualifications: List[str]
