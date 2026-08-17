from api.models.User import User
from fastapi import APIRouter, Depends
from api.schemas.user import UserResponse
from utils.security import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserResponse)
def get_current_user(current_user: User = Depends(get_current_user)):
    return current_user
