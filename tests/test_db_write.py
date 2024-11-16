from pymongo import MongoClient
import pytest
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB URI from environment
MONGO_URI = os.getenv('MONGODB_URI')

# Optionally, print to ensure the values are loaded
print("MONGO_URI:", MONGO_URI)

def test_mongodb_write():
    """Test inserting a document into the products collection."""
    try:
        # Establish connection with MongoDB
        client = MongoClient(MONGO_URI)
        db = client.shop_db  # Access the 'shop_db' database
        test_product = {"name": "Test Product", "price": 9.99}

        # Insert the test product
        result = db.products.insert_one(test_product)

        # Verify the product was inserted
        inserted_product = db.products.find_one({"_id": result.inserted_id})
        assert inserted_product is not None
        assert inserted_product["name"] == "Test Product"
        assert inserted_product["price"] == 9.99

        # Clean up: Delete the inserted test product
        db.products.delete_one({"_id": result.inserted_id})

        print("MongoDB write test passed!")
    except Exception as e:
        pytest.fail(f"MongoDB write test failed: {e}")
