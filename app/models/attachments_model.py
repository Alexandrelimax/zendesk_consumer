from pydantic import BaseModel
from typing import Optional

class Attachment(BaseModel):
    id: Optional[int] = None
    file_name: str
    content_type: str
    size: int
    url: str
    created_at: Optional[str] = None
