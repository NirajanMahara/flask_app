import pytest
from app import app

def test_home_route():
    """Test the home route for valid and invalid requests."""
    with app.test_client() as client:
        # Valid request
        response = client.get('/')
        assert response.status_code == 200

        # Invalid request
        response = client.post('/')
        assert response.status_code == 405  # Method Not Allowed
