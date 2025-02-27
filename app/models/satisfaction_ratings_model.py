from pydantic import BaseModel
from typing import Optional

class SatisfactionRating(BaseModel):
    id: Optional[int] = None
    score: str
    comment: Optional[str] = None
    created_at: Optional[str] = None
