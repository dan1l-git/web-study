from api.repositories.user_repo import UserRepository
from api.repositories.refresh_session_repo import RefreshSessionRepository
from api.schemas.user import UserCreate, UserAuth
from api.exceptions.user_exceptions import UserNotFoundError, UserAlreadyExistsError, InvalidCredentialsError
from api.utils.hash import get_password_hash, verify_password
from api.utils.jwt import create_access_token, create_refresh_token

class UserService:
    def __init__(self, user_repo: UserRepository, refresh_repo: RefreshSessionRepository):
        self.user_repo = user_repo
        self.refresh_repo = refresh_repo

    def register_user(self, user_in: UserCreate):
        user = self.user_repo.get_by_email(user_in.email)
        if user:
            raise UserAlreadyExistsError(f'User with email {user_in.email} already exists')
        user = self.user_repo.get_by_username(user_in.username)
        if user:
            raise UserAlreadyExistsError(f'User with username {user_in.username} already exists')
        password_hash = get_password_hash(user_in.password)
        user = self.user_repo.create(user_in.username, user_in.email, password_hash=password_hash)
        return user

    def authenticate_user(self, user_in: UserAuth):
        user = self.user_repo.get_by_email(user_in.email)
        if not user:
            raise InvalidCredentialsError("Invalid email or password")
        if not verify_password(user_in.password, user.password_hash):
            raise InvalidCredentialsError("Invalid email or password")
        return user

    def login(self, user_in: UserAuth):
        user = self.authenticate_user(user_in)
        data = {"sub": str(user.id)}
        access_token = create_access_token(data=data)
        refresh_token, expires_at = create_refresh_token(data=data)
        self.refresh_repo.create(user_id=user.id, refresh_token=refresh_token, expires_at=expires_at)
        return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}