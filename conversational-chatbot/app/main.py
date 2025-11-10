from fastapi import FastAPI
from app.api.v1.routes import router as api_router

app = FastAPI(title="Conversational Agent Chatbot")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Conversational Agent Chatbot API!"}