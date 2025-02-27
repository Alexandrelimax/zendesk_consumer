from pydantic import BaseModel
from typing import Optional, List

class Organization(BaseModel):
    id: Optional[int] = None
    name: str
    domain_names: List[str]
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
