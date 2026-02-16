"""
Tests for health check endpoint.
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """Test that health endpoint returns 200 OK."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root_endpoint():
    """Test that root endpoint returns API info."""
    response = client.get("/")
    assert response.status_code == 200
    assert "docs" in response.json()
