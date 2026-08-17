from fastapi import APIRouter, Depends, HTTPException
from api.database import get_db
from api.schemas.user import UserCreate
from sqlalchemy.orm import Session
from api.repositories.user_repo import UserRepository
from api.services.user_service import UserService
from api.exceptions.user_exceptions import UserAlreadyExistsError

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_user_service(db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return UserService(user_repo=user_repo)

@router.post("/register", status_code=201)
def register(user_in: UserCreate, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.register_user(user_in=user_in)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))