from fastapi import APIRouter
from app.api.v1.controllers import chatbot_controller

router = APIRouter()

@router.post("/chat")
async def chat(message: str):
    response = await chatbot_controller.process_message(message)
    return {"response": response}