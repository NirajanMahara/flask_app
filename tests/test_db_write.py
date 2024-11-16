from pymongo import MongoClient
import pytest

def test_mongodb_write():
    """Test inserting a document into the products collection."""
    from app import MONGO_URI
    try:
        client = MongoClient(MONGO_URI)
        db = client.shop_db
        test_product = {"name": "Test Product", "price": 9.99}

        # Insert the test product
        result = db.products.insert_one(test_product)

        # Verify the product was inserted
        inserted_product = db.products.find_one({"_id": result.inserted_id})
        assert inserted_product is not None
        assert inserted_product["name"] == "Test Product"

        # Clean up
        db.products.delete_one({"_id": result.inserted_id})
    except Exception as e:
        pytest.fail(f"MongoDB write test failed: {e}")
