"""add superusser

Revision ID: 65e955583171
Revises: a509b6b8b5d9
Create Date: 2021-12-06 14:39:25.674707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65e955583171'
down_revision = 'a509b6b8b5d9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('creator',
    sa.Column('is_superuser', sa.Boolean, default=False, nullable=False),
)



def downgrade():
    op.drop_column('creator', 'is_superuser')

