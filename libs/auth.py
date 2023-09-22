# auth.py
import jwt
from datetime import datetime, timedelta
from config import JWT_SECRET_KEY

def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        return payload
    except:
        return None
    
def create_jwt(profile_data: dict):
    """
    Create a JWT token based on the provided profile data.
    """
    # Define JWT payload
    payload = {
        "profile_data": profile_data,
        "exp": datetime.utcnow() + timedelta(days=1)
    }
    
    # Create JWT token
    jwt_token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    
    return jwt_token

def expire_token(token: str):
    """
    Expire the provided JWT token.
    """
    payload = verify_jwt(token)
    payload["exp"] = datetime.utcnow() - timedelta(seconds=1)
    jwt_token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    return jwt_token