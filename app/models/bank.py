import datetime
import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import backref, relation, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from app.db.base_class import Base


class Bank(Base):
    id = Column(String(36), primary_key=True, nullable=False, default=uuid.uuid4)
    account = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    creator_id = Column(String(36), ForeignKey("creator.id"), nullable=False)

    benefitsharing = relation("BenefitSharing")
