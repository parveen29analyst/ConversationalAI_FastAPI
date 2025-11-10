from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_chatbot_response():
    response = client.post("/api/v1/chat", json={"message": "Hello"})
    assert response.status_code == 200
    assert "response" in response.json()