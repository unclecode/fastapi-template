from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from libs.models import Item

router = APIRouter()

# Dependency to get the DB instance from the main app
def get_db():
    from fastapi import Request
    # Assuming the DB instance is stored in app.mongodb
    return Request.app.mongodb

@router.get("/items/")
async def get_items(db=Depends(get_db)):
    COLLECTION_NAME = "items"
    cursor = db[COLLECTION_NAME].find()
    items = await cursor.to_list(length=100)  # Converts cursor to a list, you can set the length as appropriate
    # Generate a proepr FastAPI response, with standard keys
    return {
        "status": "success",
        "items": items,
        "message": "Items retrieved successfully"
    }


@router.post("/create/")
async def create(item: Item, db=Depends(get_db)):
    COLLECTION_NAME = "items"
    # Make the booking
    await db[COLLECTION_NAME].insert_one(item.model_dump())
    
    return {
        "status": "success",
        "message": "Item created successfully"
    }
