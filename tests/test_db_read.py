from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import pytest
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB URI from environment
MONGO_URI = os.getenv('MONGODB_URI')

# Optionally, print to ensure the values are loaded
print("MONGO_URI:", os.getenv('MONGODB_URI'))


# @pytest.fixture(scope='module')
# def mongodb_client():
#     """Fixture to set up MongoDB client."""
#     client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
#     yield client
#     client.close()

def test_mongodb_connection():
    """Test MongoDB connection using the ping command."""
    from app import MONGO_URI
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')  # Ping MongoDB
        print("MongoDB connection successful!")
    except ServerSelectionTimeoutError:
        pytest.fail("MongoDB connection failed: Server not reachable or invalid URI")
    except Exception as e:
        pytest.fail(f"MongoDB connection failed: {e}")
