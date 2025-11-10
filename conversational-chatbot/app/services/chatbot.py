from typing import List, Dict

class ChatbotService:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "bye": "Goodbye! Have a great day!",
            "how are you?": "I'm just a computer program, but thanks for asking!",
        }

    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower()
        return self.responses.get(user_input, "I'm sorry, I don't understand that.")

    def process_message(self, message: str) -> Dict[str, str]:
        response = self.get_response(message)
        return {
            "user_message": message,
            "bot_response": response
        }

    def get_all_responses(self) -> List[str]:
        return list(self.responses.values())