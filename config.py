import os
SECRET_KEY = os.urandom(32)

WTF_CSRF_ENABLED = False

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode
DEBUG = True

# Connect to the database

# DONE IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://Bao:123@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLACHEMY_ECHO = True
