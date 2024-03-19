from pydantic import BaseModel
from typing import List, Optional


class BookIn(BaseModel):
    name: str
    language: str
    year: int


class BookOut(BookIn):
    id: int


class BookUpdate(BookIn):
    name: Optional[str] = None
    language: Optional[str] = None
    year: Optional[int] = None
