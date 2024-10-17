# CSD-4503-02
The code base of the course CSD 4503.

# E-Commerce Flask Application

This is a simple e-commerce Flask application that displays product information from a MongoDB Atlas database.

## Features

- Homepage with a brief introduction
- Products page displaying items from MongoDB
- Responsive design using Bootstrap
- Custom styling

## App Preview
<img src="static/images/Screenshot 2024-10-12 at 4.21.11 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-12 at 4.22.23 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-12 at 4.23.33 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-12 at 4.26.15 PM.png" width="250" />
<img src="static/images/Screenshot 2024-10-12 at 4.27.00 PM.png" width="250" />

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/NirajanMahara/flask_app.git
   cd flask_app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Mac 
   use 
   venv\Scripts\activate # On Windows
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your MongoDB Atlas database and update the `.env` file with your connection string.

##### Set Up Instructions
To run the application, you have to create a ".env" file locally.
This file must include two variables called ```"MONGODB_USERNAME"``` and ```"MONGODB_PASSWORD"```,
which can be MongoDB Atlas credentials. 

5. Run the application:
   ```
   python app.py
   ```

Open a web browser and navigate to `http://localhost:5000`


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

