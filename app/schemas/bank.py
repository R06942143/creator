from typing import Optional
from datetime import datetime
import uuid
from pydantic import BaseModel, validator

from app.schemas.creator import Creator


# Shared properties
class BankBase(BaseModel):
    account: str
    created_at: datetime
    update_at: datetime
    creator_id: str

    # @validator('bank')
    # def check_bank(cls, v):
    #     if v is None:
    #         return v

    #     if "https://www.facebook.com" not in v:
    #         raise ValueError('Please provide a valid facebook link')
    #     return v


# Properties to receive via API on creation
class BankCreate(BankBase):
    pass


# Properties to receive via API on update
class BankUpdate(BankBase):
    pass


class BankInDBBase(BankBase):
    id: Optional[str] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Bank(BankInDBBase):
    pass


# Additional properties stored in DB
class BankInDB(BankInDBBase):
    pass
