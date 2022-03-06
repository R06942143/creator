# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.bank import Bank  # noqa
from app.models.creator import Creator  # noqa
from app.models.link import Link  # noqa
from app.models.benefitsharing import BenefitSharing  # noqa