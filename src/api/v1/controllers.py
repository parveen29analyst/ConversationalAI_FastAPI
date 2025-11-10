from fastapi import APIRouter, HTTPException
from src.schemas.message import MessageSchema
from src.services.chatbot import ChatbotService

router = APIRouter()
chatbot_service = ChatbotService()

@router.post("/chat", response_model=MessageSchema)
async def chat(message: MessageSchema):
    try:
        response = chatbot_service.get_response(message.text)
        return MessageSchema(text=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))