from fastapi import FastAPI, Query, Request, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse
import  uvicorn
from libs.db_operations import startup_db_client, shutdown_db_client, setup_db
from libs.db_operations import startup_db_client, shutdown_db_client, setup_db
from libs.models import Item, Login
from libs.middleware import verify_session
from libs.auth import create_jwt, expire_token
from libs.app_setup import setup_app
from libs.app_logger import logger
from routes.item_routes import router as item_router
from routes.auth_routes import router as auth_router
import config

app = FastAPI()
setup_db(app) 
setup_app(app, logger)
app.include_router(item_router, prefix="/v1/items")
app.include_router(auth_router, prefix="/v1/auth")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
    
app.middleware("http")(verify_session)
# Register the startup and shutdown events
app.add_event_handler("startup", startup_db_client)
app.add_event_handler("shutdown", shutdown_db_client)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Run FastAPI on port 8080
if __name__ == "__main__":
    uvicorn.run("app:app", host=config.HOST, port=config.PORT, reload=config.RELOAD)