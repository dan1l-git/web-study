from api.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class RefreshSession(Base):
    __tablename__ = 'refresh_session'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    refresh_token = Column(String, index=True)
    expires_at = Column(DateTime)