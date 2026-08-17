from api.configuration import Configuration
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException

import jwt

settings = Configuration()

JWT_SECRET = settings.JWT_SECRET_KEY
JWT_ALGORITHM = settings.JWT_ALGORITHM

def create_access_token(data: dict):
    to_encode = data.copy()
    expire_access_token = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({'exp': expire_access_token})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire_refresh_token = datetime.now(timezone.utc) + timedelta(days=7)
    to_encode.update({'exp': expire_refresh_token})

    token = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token, expire_refresh_token

def validate_token(token: str):
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return payload