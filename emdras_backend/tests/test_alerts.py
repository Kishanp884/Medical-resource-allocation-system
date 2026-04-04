import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_alert():
    response = client.post("/alerts", json={"type": "Flood", "severity": "High", "location": "Chennai"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Alert created"}

def test_get_alerts():
    response = client.get("/alerts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)