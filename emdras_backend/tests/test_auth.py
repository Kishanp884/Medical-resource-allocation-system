import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login():
    response = client.post("/login", json={"username": "test", "password": "pass", "role": "admin"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Login successful"}