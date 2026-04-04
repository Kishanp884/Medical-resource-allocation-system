import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_iv():
    response = client.post("/iv", json={"patient_id": "P1", "flow_rate": 10.5, "volume": 100.0})
    assert response.status_code == 200
    assert response.json() == {"msg": "IV data added"}

def test_get_iv():
    response = client.get("/iv")
    assert response.status_code == 200
    assert isinstance(response.json(), list)