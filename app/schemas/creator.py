from datetime import datetime
from typing import Optional
import uuid
from .link import Link
from pydantic import BaseModel, EmailStr, validator
from phonenumbers import (
    NumberParseException,
    PhoneNumberFormat,
    PhoneNumberType,
    format_number,
    is_valid_number,
    number_type,
    parse as parse_phone_number,
)

MOBILE_NUMBER_TYPES = PhoneNumberType.MOBILE, PhoneNumberType.FIXED_LINE_OR_MOBILE


# Shared properties
class CreatorBase(BaseModel):
    account: str
    phone: str
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    # is_superuser: bool = False
    nick_name: Optional[str] = None
    brief_introduction: Optional[str] = None
    work_experience: Optional[str] = None
    case_type: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    @validator('phone')
    def check_phone(cls, v):
        if v is None:
            return v

        try:
            n = parse_phone_number(v, "TW")
        except NumberParseException as e:
            raise ValueError('Please provide a valid mobile phone number') from e

        if not is_valid_number(n) or number_type(n) not in MOBILE_NUMBER_TYPES:
            raise ValueError('Please provide a valid mobile phone number')

        return format_number(
            n, PhoneNumberFormat.NATIONAL if n.country_code == 886
            else PhoneNumberFormat.INTERNATIONAL)

    class Config:
        orm_mode = True


# Properties to receive via API on creation
class CreatorCreate(CreatorBase):
    pwd: str


# Properties to receive via API on update
class CreatorUpdate(CreatorBase):
    pwd: Optional[str] = None


class CreatorInDBBase(CreatorBase):
    id: Optional[str] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Creator(CreatorInDBBase):
    pass


# Additional properties stored in DB
class CreatorInDB(CreatorInDBBase):
    hashed_password: str
