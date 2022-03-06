import datetime
import uuid
from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relation
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Text
from app.db.base_class import Base


class Creator(Base):
    id = Column(String(36), primary_key=True, nullable=False, default=uuid.uuid4)
    account = Column(String(50), unique=True, nullable=False)
    pwd = Column(String(60), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)
    nick_name = Column(String(50))
    brief_introduction = Column(Text())
    work_experience = Column(Text())
    case_type = Column(String(50))

    link = relation("Link")
    bank = relation("Bank")
