# middleware.py
from fastapi import HTTPException, Request
from fastapi.responses import RedirectResponse
from libs.auth import verify_jwt

async def verify_session_by_header(request: Request, call_next):
    jwt_token = request.headers.get("Authorization")
    payload = verify_jwt(jwt_token)
    if payload:
        response = await call_next(request)
        return response
    else:
        # Redirect to login page if JWT is missing or invalid
        return RedirectResponse(url="/v1/auth/login/")
        # raise HTTPException(status_code=401, detail="Unauthorized")

async def _verify_session(request: Request, call_next):
    jwt_token = request.query_params.get("token")
    payload = verify_jwt(jwt_token)
    if True or payload:
        request.state.payload = payload  # You can store the payload in the request state for later use.
        response = await call_next(request)
        return response
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")

async def verify_session(request: Request, call_next):
    if request.url.path == "/":
        # Only verify JWT for the root path
        jwt_token = request.query_params.get("token")
        payload = verify_jwt(jwt_token)
        if payload:
            request.state.payload = payload  # You can store the payload in the request state for later use.
            response = await call_next(request)
            return response
        else:
            # Redirect to login page if JWT is missing or invalid
            return RedirectResponse(url="/v1/auth/login/")
            # raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        # Skip JWT verification for static files and certain routes
        response = await call_next(request)
        return response
