from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Conversational Chatbot"
    api_version: str = "v1"
    debug: bool = False
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()