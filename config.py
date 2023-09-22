# config.py
import os
from dotenv import load_dotenv
load_dotenv()

DB_URI = os.environ.get("DB_URI")
DB_NAME = os.environ.get("DB_NAME")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
PORT = 8000
HOST = "0.0.0.0"
RELOAD = True