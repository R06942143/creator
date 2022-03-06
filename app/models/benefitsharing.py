import datetime
import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relation
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float
from app.db.base_class import Base


class BenefitSharing(Base):
    id = Column(String(36), primary_key=True, nullable=False, default=uuid.uuid4())
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    bank_id = Column(String(36), ForeignKey("bank.id"), nullable=False)
    amount = Column(Float(), nullable=False)
    is_paid = Column(Boolean, default=False, nullable=False)
