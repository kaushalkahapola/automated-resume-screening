from pydantic import BaseModel, Field
from typing import List

class JobDescription(BaseModel):
    title: str = Field(...)
    skills: List[str] = Field(...)
    description: str = Field(...)