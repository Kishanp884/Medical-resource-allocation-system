import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_organ():
    response = client.post("/organs", json={"organ_id": "O1", "type": "Kidney", "blood_group": "A+", "location": "Chennai", "status": "Available"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Organ added"}

def test_get_organs():
    response = client.get("/organs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)