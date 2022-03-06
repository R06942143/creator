import datetime
import uuid
from sqlalchemy import Column, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

from app.db.base_class import Base


class Link(Base):
    id = Column(String(36), primary_key=True, nullable=False, default=uuid.uuid4())
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    facebook = Column(String(100))
    instagram = Column(String(100))
    blog = Column(String(100))
    youtube = Column(String(100))
    creator_id = Column(String(36), ForeignKey("creator.id"), nullable=False)
