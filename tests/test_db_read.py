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
print("MONGO_URI:", MONGO_URI)

def test_mongodb_connection():
    """Test MongoDB connection using the ping command."""
    try:
        # Connect to MongoDB with a timeout of 5 seconds
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        
        # Ping MongoDB server
        client.admin.command('ping')
        
        print("MongoDB connection successful!")
    except ServerSelectionTimeoutError:
        pytest.fail("MongoDB connection failed: Server not reachable or invalid URI")
    except Exception as e:
        pytest.fail(f"MongoDB connection failed: {e}")
