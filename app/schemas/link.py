from datetime import datetime
from typing import Optional
import uuid

from pydantic import BaseModel, validator


# Shared properties
class LinkBase(BaseModel):
    facebook: Optional[str] = None
    instagram: Optional[str] = None
    blog: Optional[str] = None
    youtube: Optional[str] = None
    creator_id: str

    @validator('facebook')
    def check_facebook(cls, v):
        if v is None:
            return v

        if "https://www.facebook.com" not in v:
            raise ValueError('Please provide a valid facebook link')
        return v

    @validator('instagram')
    def check_instagram(cls, v):
        if v is None:
            return v

        if "https://www.instagram.com" not in v:
            raise ValueError('Please provide a valid instagram link')
        return v

    @validator('youtube')
    def check_youtube(cls, v):
        if v is None:
            return v

        if "https://www.youtube.com" not in v:
            raise ValueError('Please provide a valid youtube link')
        return v


# Properties to receive via API on creation
class LinkCreate(LinkBase):
    pass


# Properties to receive via API on update
class LinkUpdate(LinkBase):
    update_at: datetime
    pass


class LinkInDBBase(LinkBase):
    id: Optional[str] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Link(LinkInDBBase):
    pass


# Additional properties stored in DB
class LinkInDB(LinkInDBBase):
    pass
