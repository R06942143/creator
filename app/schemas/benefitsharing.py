from typing import Optional
from datetime import datetime
import uuid
from pydantic import BaseModel, validator
from app.schemas.bank import Bank

from app.schemas.creator import Creator


# Shared properties
class BenefitSharingBase(BaseModel):
    amount: float
    created_at: datetime
    update_at: datetime
    bank_id: str
    is_paid: bool

    # @validator('bank')
    # def check_bank(cls, v):
    #     if v is None:
    #         return v

    #     if "https://www.facebook.com" not in v:
    #         raise ValueError('Please provide a valid facebook link')
    #     return v


# Properties to receive via API on creation
class BenefitSharingCreate(BenefitSharingBase):
    pass


# Properties to receive via API on update
class BenefitSharingUpdate(BenefitSharingBase):
    pass


class BenefitSharingInDBBase(BenefitSharingBase):
    id: Optional[str] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class BenefitSharing(BenefitSharingInDBBase):
    pass


# Additional properties stored in DB
class BenefitSharingInDB(BenefitSharingInDBBase):
    pass
