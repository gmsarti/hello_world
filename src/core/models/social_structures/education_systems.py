from pydantic import BaseModel
from typing import List

class EducationSystem(BaseModel):
 name: str
 levels: List[str]
 students: int
