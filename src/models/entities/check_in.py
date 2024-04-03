from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from ..settings.base import Base

class CheckIn(Base):
    __tablename__ = 'tb_check_ins'

    id  = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    attendee_id = Column(String, ForeignKey('tb_attendees.id'))
    created_at = Column(DateTime, nullable=False, default=func.now())

    #def __repr__(self) -> str:
    #    return f'CheckIn [attendee={self.attendee_id}, created_at={self.created_at}]'
