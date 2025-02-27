from pydantic import BaseModel
from typing import Optional

class Conversation(BaseModel):
    id: Optional[int] = None
    subject: str
    messages_count: int
    status: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
