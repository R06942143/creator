# from .crud_item import item
# from .crud_user import user
from .crud_creator import creator
# For a new basic set of CRUD operations you could just do

from .base import CRUDBase
from app.models.link import Link
from app.schemas.link import LinkCreate, LinkUpdate
from app.models.bank import Bank
from app.schemas.bank import BankCreate, BankUpdate
from app.models.benefitsharing import BenefitSharing
from app.schemas.benefitsharing import BenefitSharingCreate, BenefitSharingUpdate

link = CRUDBase[Link, LinkCreate, LinkUpdate](Link)
bank = CRUDBase[Bank, BankCreate, BankUpdate](Bank)
benefitsharing = CRUDBase[BenefitSharing, BenefitSharingCreate, BenefitSharingUpdate](BenefitSharing)
