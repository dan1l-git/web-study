from api.repositories.user_repo import UserRepository
from api.schemas.user import UserCreate
from api.exceptions.user_exceptions import UserNotFoundError, UserAlreadyExistsError
from api.utils.hash import get_password_hash

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

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