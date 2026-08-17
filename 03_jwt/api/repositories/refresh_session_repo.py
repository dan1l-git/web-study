from datetime import datetime

from sqlalchemy.orm import Session
from api.models.RefreshSession import RefreshSession

class RefreshSessionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int, refresh_token: str, expires_at: datetime):
        refresh_session = RefreshSession(user_id=user_id, refresh_token=refresh_token, expires_at=expires_at)
        self.db.add(refresh_session)
        self.db.commit()
        self.db.refresh(refresh_session)

        return refresh_session

    def get_by_token(self, refresh_token: str):
        return self.db.query(RefreshSession).filter(RefreshSession.refresh_token == refresh_token).first()

    def delete(self, refresh_session: RefreshSession):
        self.db.delete(refresh_session)
        self.db.commit()