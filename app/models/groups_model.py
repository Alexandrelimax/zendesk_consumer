from pydantic import BaseModel
from typing import Optional

class Group(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
