from sqlalchemy import Column, DateTime, String

from ..settings.base import Base

class Attendee(Base):
    __tablename__ = 'tb_attendees'

    id  = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
