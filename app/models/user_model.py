from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    role: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
