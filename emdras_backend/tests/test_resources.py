import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_resource():
    response = client.post("/resources", json={"hospital": "Apollo", "beds": 20, "ventilators": 5, "status": "Available"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Resource added"}

def test_get_resources():
    response = client.get("/resources")
    assert response.status_code == 200
    assert isinstance(response.json(), list)