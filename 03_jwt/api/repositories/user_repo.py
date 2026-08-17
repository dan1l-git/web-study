from sqlalchemy.orm import Session
from api.models.User import User
from api.schemas.user import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, username: str, email: str, password_hash: str):
        db_user = User(username=username, email=email, password_hash=password_hash)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_by_email(self, email: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            return None
        return user

    def get_by_username(self, username: str):
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            return None
        return user

    def get_by_id(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        return user