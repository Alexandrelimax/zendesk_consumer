from pydantic import BaseModel
from typing import Optional

class Ticket(BaseModel):
    id: Optional[int] = None
    subject: str
    description: str
    status: str
    priority: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
