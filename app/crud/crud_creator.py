from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.creator import Creator
from app.schemas.creator import CreatorCreate, CreatorUpdate


class CRUDUser(CRUDBase[Creator, CreatorCreate, CreatorUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[Creator]:
        return db.query(Creator).filter(Creator.email == email).first()

    def get_by_account(self, db: Session, *, account: str) -> Optional[Creator]:
        return db.query(Creator).filter(Creator.account == account).first()

    def create(self, db: Session, *, obj_in: CreatorCreate) -> Creator:
        db_obj = Creator(
            email=obj_in.email,
            account=obj_in.account,
            phone=obj_in.phone,
            is_active=obj_in.is_active,
            nick_name=obj_in.nick_name,
            brief_introduction=obj_in.brief_introduction,
            work_experience=obj_in.work_experience,
            case_type=obj_in.case_type,
            pwd=get_password_hash(obj_in.pwd)
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Creator,
        obj_in: Union[CreatorUpdate, Dict[str, Any]]
    ) -> Creator:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["pwd"]:
            hashed_password = get_password_hash(update_data["pwd"])
            del update_data["pwd"]
            update_data["pwd"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, account: str, password: str) -> Optional[Creator]:
        creator = self.get_by_account(db, account=account)
        if not creator:
            return None
        if not verify_password(password, creator.pwd):
            return None
        return creator

    def is_active(self, creator: Creator) -> bool:
        return creator.is_active

    def is_superuser(self, creator: Creator) -> bool:
        return creator.is_superuser


creator = CRUDUser(Creator)
