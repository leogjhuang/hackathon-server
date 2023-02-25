import os

from flask import Flask
from app.database import init_db, load_data


# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')

# Initialize the database
init_db(app)
load_data(app)

# Import the routes
from app.routes import *
