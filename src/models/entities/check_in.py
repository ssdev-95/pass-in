from sqlalchemy import Column, DateTime, Integer, String

from ..settings.base import Base

class CheckIn(Base):
    __tablename__ = 'tb_check_ins'

    id  = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    attendee_id = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
