from pydantic import BaseModel
from typing import Optional

class Call(BaseModel):
    id: Optional[int] = None
    from_number: str
    to_number: str
    duration: int
    status: str
    created_at: Optional[str] = None
