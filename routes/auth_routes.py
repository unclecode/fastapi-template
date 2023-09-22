from fastapi import APIRouter, HTTPException, Depends, Request, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from libs.auth import create_jwt, expire_token

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Dependency to get the DB instance from the main app
def get_db():
    from fastapi import Request
    # Assuming the DB instance is stored in app.mongodb
    return Request.app.mongodb

@router.get("/login/")
def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login/")
async def login(student_id: str = Form(...), email: str = Form(...)):
    # Apply the logic to authenticate the user
    response = {
        "status_code": 200,
        "json": lambda: {"name": "John Doe", "student_id": student_id, "email": email}
    }
    
    if response["status_code"] == 200:
        profile_data = response["json"]()
        jwt_token = create_jwt(profile_data)
        return JSONResponse(content={"redirect_url": f"/?token={jwt_token}&student_id={student_id}"})
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")

@router.get("/logout/")
def logout(request: Request):
    # Expire the JWT token by setting the expiry time to 1 second ago
    jwt_token = request.query_params.get("token")
    jwt_token = expire_token(jwt_token)  # You'll need to implement this function
    return RedirectResponse(url=f"/v1/auth/login/")