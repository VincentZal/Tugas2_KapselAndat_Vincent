from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "username": "staff01",
        "email": "staff01@example.com",
        "password": "Password1!",
        "role": "staff"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "staff01"
    assert data["role"] == "staff"
