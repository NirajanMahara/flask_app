# CSD-4503-02

The code base of the course CSD 4503, focused on creating and deploying a full-stack e-commerce application using Flask, MongoDB, and CI/CD practices.

## E-Commerce Flask Application

This project is a simple e-commerce web application built with Flask. It displays product information stored in a MongoDB Atlas database and includes features such as data management, unit testing, and CI/CD pipeline integration for continuous deployment.

## Key Features

- **Homepage** with a brief introduction
- **Products page** displaying items from MongoDB
- **Responsive design** using Bootstrap
- **Custom styling**
- **MongoDB Integration**: Retrieve and display products stored in MongoDB
- **Unit Tests**: Ensures proper functioning of MongoDB connection and CRUD operations
- **CI/CD Pipeline**: GitHub Actions workflow for continuous integration and deployment
- **Profile Management**: Option to upload and edit user profile pictures
- **Secure User Authentication**: Implemented with JWT tokens for session management

## App Preview
<img src="static/images/Screenshot 2024-10-12 at 4.21.11 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-12 at 4.22.23 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-12 at 4.23.33 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-12 at 4.26.15 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-12 at 4.27.00 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-17 at 12.38.37 AM.png" width="750" />
<img src="static/images/Screenshot 2024-10-17 at 12.35.18 AM.png" width="750" />
<img src="static/images/Screenshot 2024-10-17 at 12.40.49 AM.png" width="750" />

updated preview & the script to add the data to MongoDB 
<img src="static/images/Screenshot 2024-10-19 at 11.56.28 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-19 at 11.57.27 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-19 at 11.58.32 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-19 at 11.59.33 PM.png" width="250" />

<img src="static/images/Screenshot 2024-11-16 at 4.49.53 PM.png" width="250" />
<img src="static/images/Screenshot 2024-11-16 at 4.51.17 PM.png" width="250" />
<img src="static/images/Screenshot 2024-11-16 at 4.53.34 PM.png" width="250" />

Flask CI/CD pipeline run tests completed successfully
<img src="static/images/ci-test complete Screenshot 2024-11-16 at 5.16.37 PM.png" width="750" />

## Setup

To run this application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NirajanMahara/flask_app.git
   cd flask_app
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Mac 
   venv\Scripts\activate  # On Windows
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your MongoDB Atlas database:**
   - Create a MongoDB Atlas account and set up a cluster.
   - Obtain your connection string from MongoDB Atlas and create a `.env` file in the project root.

   The `.env` file should contain the following variables:
   ```env
   MONGODB_USERNAME=mongodb_username
   MONGODB_PASSWORD=mongodb_password
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the app:**
   - Open a web browser and navigate to `http://localhost:5000`

## MongoDB Data Management

This project includes a script (`add_data_mongodb.py`) for adding product data to your MongoDB Atlas database. You can use this script to insert product details into your `products` collection. It requires the following environment variables:

- `MONGODB_USERNAME`
- `MONGODB_PASSWORD`

### `add_data_mongodb.py`

```python
# The script to add the data to MongoDB

from pymongo import MongoClient  # pip install pymongo
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
    products_collection = db.products  # products is the name of the collection inside the database
    print("MongoDB connection successful!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Example product objects
products = [
    {
        "name": "Product 1",
        "image_path": "images/product1.jpg",  # images/product.jpg
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
```

### How to Use

1. **Add Data to MongoDB:**
   - Set up your MongoDB Atlas credentials in the `.env` file.
   - Run the script to add sample products to the database:
   ```bash
   python add_data_mongodb.py
   ```

2. **Verify Data in MongoDB:**
   - After running the script, your products should be added to the `shop_db` database in the `products` collection.
   - You can verify this by checking the MongoDB Atlas dashboard.

## CI/CD Pipeline

This project integrates a **CI/CD pipeline** using **GitHub Actions**. The pipeline automates:

- **Testing**: Runs unit tests using `pytest` to ensure the application is functioning correctly.
- **Deployment**: Automatically deploys changes to the server when the `main` branch is updated.

### GitHub Actions Workflow

The `.github/workflows/ci.yml` file contains the CI/CD configuration, including steps for setting up Python, installing dependencies, running tests, and deploying the application.

### Example of Workflow:
```yaml
name: Flask App CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt
      - name: Run tests
        run: |
          source venv/bin/activate
          pytest tests/
```

## Testing

The application includes unit tests to validate the following:

- **MongoDB Connection**: Ensures the application can connect to MongoDB and retrieve data.
- **Data Insertion**: Validates that new product entries can be inserted into the database.
- **Profile Image Upload**: Ensures users can upload and view profile images.

Run tests using:
```bash
pytest tests/
```

## Contributing

Contributions are welcome! If you'd like to contribute, feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Create a new pull request

For major changes, please open an issue first to discuss what you'd like to change.
