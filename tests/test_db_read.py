from pymongo import MongoClient
import pytest

def test_mongodb_connection():
    """Test MongoDB connection using the ping command."""
    from app import MONGO_URI
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')  # Ping MongoDB
        assert True  # If ping succeeds
    except Exception as e:
        pytest.fail(f"MongoDB connection failed: {e}")
