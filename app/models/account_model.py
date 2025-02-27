from pydantic import BaseModel
from typing import Optional

class Account(BaseModel):
    id: Optional[int] = None
    name: str
    domain: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
