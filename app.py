"""
Flask E-Commerce Application

This script runs a Flask web application that displays product information
from a MongoDB Atlas database. It includes routes for a homepage and a products page.

Author: Nirajan Mahara
Date: Nov 16, 2024
"""
# Run this command in the terminal to install flask framework:
# pip install flask

from flask import Flask, render_template
from pymongo import MongoClient # pip install pymongo
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
MONGO_URI = os.getenv('MONGODB_URI')  # from the .env file

# Initialize Flask application
app = Flask(__name__)

# # Access environment variables
# MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
# MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

# # Construct MongoDB connection string using environment variables
# MONGO_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.iw3gq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# Initialize MongoDB Atlas Client
try:
    client = MongoClient(MONGO_URI)
    db = client.shop_db  # shop_db is the name of the database in MongoDB Atlas
    products_collection = db.products #products is the name of the collection inside the database
    print("MongoDB connection successful!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Define routes
@app.route('/')
def home():
    """Route for the homepage."""
    return render_template('home.html')

@app.route('/products')
def products():
    """Route for the products page. Fetches products from MongoDB and passes them to the template."""
    try:
        products = list(products_collection.find())
        # Convert ObjectId to string for each product
        for product in products:
            product['_id'] = str(product['_id'])
        return render_template('products.html', products=products)
    except Exception as e:
        # Log the error (in a production app
        print(f"Error fetching products: {e}")
        # Return an error page or message
        return "An error occurred while fetching products. Please try again later.", 500
         

if __name__ == '__main__':
    app.run(debug=True)
    