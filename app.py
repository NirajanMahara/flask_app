"""
Flask E-Commerce Application

This script runs a Flask web application that displays product information
from a MongoDB Atlas database. It includes routes for a homepage and a products page.

Author: Nirajan Mahara
Date: Oct 12, 2024
"""

from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Setup MongoDB Atlas connection
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.get_database('shop_db')  # This will use the database specified in the connection string
products_collection = db.products

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
    