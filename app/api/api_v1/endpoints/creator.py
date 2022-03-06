from datetime import datetime
from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from sqlalchemy.sql import schema

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email

router = APIRouter()


@router.get("/", response_model=List[schemas.Creator])
def read_creators(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_creator: models.Creator = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users. For superuser.
    """
    creators = crud.creator.get_multi(db, skip=skip, limit=limit)
    return creators


@router.post("/", response_model=schemas.Creator)
def create_creator(
    *,
    db: Session = Depends(deps.get_db),
    creator_in: schemas.CreatorCreate,
    current_creator: models.Creator = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new user. For superuser.
    """
    creator = crud.creator.get_by_email(db, email=creator_in.email)
    if creator:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    creator = crud.creator.create(db, obj_in=creator_in)
    if settings.EMAILS_ENABLED and creator_in.email:
        send_new_account_email(
            email_to=creator_in.email, username=creator_in.account, password=creator_in.pwd
        )
    return creator


@router.put("/me", response_model=schemas.Creator)
def update_creator_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    nick_name: str = Body(None),
    email: EmailStr = Body(None),
    phone: str = Body(None),
    brief_introduction: str = Body(None),
    current_creator: models.Creator = Depends(deps.get_current_active_creator),
) -> Any:
    """
    Update own user.
    """
    current_creator_data = jsonable_encoder(current_creator)
    creator_in = schemas.CreatorUpdate(**current_creator_data)
    if password is not None:
        creator_in.pwd = password
    if nick_name is not None:
        creator_in.nick_name = nick_name
    if email is not None:
        creator_in.email = email
    if brief_introduction is not None:
        creator_in.brief_introduction = brief_introduction
    if phone is not None:
        creator_in.phone = phone
    creator = crud.creator.update(db, db_obj=current_creator, obj_in=creator_in)
    return creator


@router.get("/me", response_model=schemas.Creator)
def read_creator_me(
    db: Session = Depends(deps.get_db),
    current_creator: models.Creator = Depends(deps.get_current_active_creator),
) -> Any:
    """
    Get current user.
    """
    return current_creator


@router.post("/open", response_model=schemas.Creator)
def create_creator_open(
    *,
    db: Session = Depends(deps.get_db),
    phone: str = Body(...),
    password: str = Body(...),
    email: EmailStr = Body(...),
    account: str = Body(...),
    nick_name: str = Body(None),
    brief_introduction: str = Body(None),
    work_exerience: str = Body(None),
    case_type: str = Body(None)
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    creator = crud.creator.get_by_account(db, account=account)
    if creator:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    creator = crud.creator.get_by_email(db, email=email)
    if creator:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )

    try:
        user_in = schemas.CreatorCreate(
            account=account, phone=phone, email=email,
            nick_name=nick_name, brief_introduction=brief_introduction,
            work_exerience=work_exerience, case_type=case_type,
            pwd=password
        )
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail='Please provide a valid mobile phone number',
        )

    creator = crud.creator.create(db, obj_in=user_in)

    return creator
