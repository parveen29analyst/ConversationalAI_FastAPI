from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    id: Optional[int]
    user_id: int
    content: str
    timestamp: Optional[str] = None

class MessageCreate(BaseModel):
    user_id: int
    content: str

class MessageResponse(BaseModel):
    id: int
    user_id: int
    content: str
    timestamp: str

    class Config:
        orm_mode = True