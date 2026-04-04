import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_stats():
    response = client.get("/analytics")
    assert response.status_code == 200
    assert "total_alerts" in response.json()