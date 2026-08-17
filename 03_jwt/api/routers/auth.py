from fastapi import APIRouter, Depends, HTTPException
from api.database import get_db
from api.schemas.user import UserCreate, UserAuth, RefreshTokenRequest
from sqlalchemy.orm import Session
from api.repositories.user_repo import UserRepository
from api.services.user_service import UserService
from api.repositories.refresh_session_repo import RefreshSessionRepository
from api.exceptions.user_exceptions import UserAlreadyExistsError, InvalidCredentialsError, InvalidTokenError

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_user_service(db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    refresh_repo = RefreshSessionRepository(db)
    return UserService(user_repo=user_repo, refresh_repo=refresh_repo)

@router.post("/register", status_code=201)
def register(user_in: UserCreate, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.register_user(user_in=user_in)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user_in: UserAuth, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.login(user_in=user_in)
    except InvalidCredentialsError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/refresh")
def refresh(body: RefreshTokenRequest, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.refresh_token(refresh_token=body.refresh_token)
    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/logout")
def logout(body: RefreshTokenRequest, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.logout(body.refresh_token)
    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=str(e))