from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.sql import func

from ..settings.base import Base

class Attendee(Base):
    __tablename__ = 'tb_attendees'

    id  = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, ForeignKey('tb_events.id'))
    created_at = Column(DateTime, default=func.now())

