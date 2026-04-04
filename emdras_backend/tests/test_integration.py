import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_integration_alert_resource():
    # Clear any existing data if needed, but since in-memory, ok
    # Post alert
    client.post("/alerts", json={"type": "Flood", "severity": "High", "location": "Chennai"})
    # Post resource
    client.post("/resources", json={"hospital": "Apollo", "beds": 20, "ventilators": 5, "status": "Available"})
    # Get alerts
    response = client.get("/alerts")
    assert len(response.json()) >= 1
    # Get resources
    response = client.get("/resources")
    assert len(response.json()) >= 1