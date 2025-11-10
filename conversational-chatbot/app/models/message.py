from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    id: Optional[int] = None
    user_id: int
    content: str
    timestamp: str

class ResponseMessage(BaseModel):
    message_id: int
    response_content: str
    timestamp: str