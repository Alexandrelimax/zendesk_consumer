from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    id: Optional[int] = None
    sender_id: int
    recipient_id: int
    content: str
    created_at: Optional[str] = None
