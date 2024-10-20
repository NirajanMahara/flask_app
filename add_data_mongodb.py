# The script to add the data to MongoDB

from pymongo import MongoClient # pip install pymongo
import os
from dotenv import load_dotenv
load_dotenv()

# Access environment variables
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
# Construct MongoDB connection string using environment variables
MONGO_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.iw3gq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Initialize MongoDB Atlas Client
try:
    client = MongoClient(MONGO_URI)
    db = client.shop_db  # shop_db is the name of the database in MongoDB Atlas
    products_collection = db.products #products is the name of the collection inside the database
    print("MongoDB connection successful!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Example product objects
products = [
    {
        "name": "Product 1",
        "image_path": "images/product1.jpg", # images/product.jpg
        "price": 29.99,
        "tag": "New"
    },
    {
        "name": "Product 2",
        "image_path": "images/product2.jpg",
        "price": 49.99,
        "tag": "Discounted"
    },
    {
        "name": "Product 3",
        "image_path": "images/product3.jpg",
        "price": 19.99,
        "tag": "Best Seller"
    },
    {
        "name": "Product 5",
        "image_path": "images/product5.jpg",
        "price": 69.99,
        "tag": "Black Friday"
    }
]
# Insert the products into MongoDB
products_collection.insert_many(products)  # allows you to add a list of dictionaries into the database
