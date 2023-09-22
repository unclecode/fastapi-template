from motor.motor_asyncio import AsyncIOMotorClient
from config import DB_URI, DB_NAME

app = None  # Initialize a global variable for the FastAPI app

def setup_db(fastapi_app):
    global app
    app = fastapi_app

async def startup_db_client():
    global app
    app.mongodb_client = AsyncIOMotorClient(DB_URI)
    app.mongodb = app.mongodb_client.get_database(DB_NAME)

async def shutdown_db_client():
    global app
    app.mongodb_client.close()
