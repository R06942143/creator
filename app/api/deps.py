from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_creator(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.Creator:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    creator = crud.creator.get(db, id=token_data.sub)
    if not creator:
        raise HTTPException(status_code=404, detail="User not found")
    return creator


def get_current_active_creator(
    current_creator: models.Creator = Depends(get_current_creator),
) -> models.Creator:
    if not crud.creator.is_active(current_creator):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_creator


def get_current_active_superuser(
    current_creator: models.Creator = Depends(get_current_creator),
) -> models.Creator:
    if not crud.creator.is_superuser(current_creator):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_creator
