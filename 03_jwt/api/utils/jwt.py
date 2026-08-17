from api.configuration import Configuration
from datetime import datetime, timedelta, timezone
import jwt

settings = Configuration()

JWT_SECRET = settings.JWT_SECRET_KEY

def create_access_token(data: dict):
    to_encode = data.copy()
    expire_access_token = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({'exp': expire_access_token})
    return jwt.encode(
        to_encode,
        JWT_SECRET,
        algorithm="HS256"
    )

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire_refresh_token = datetime.now(timezone.utc) + timedelta(days=7)
    to_encode.update({'exp': expire_refresh_token})

    token = jwt.encode(
        to_encode,
        JWT_SECRET,
        algorithm="HS256"
    )
    return token, expire_refresh_token
