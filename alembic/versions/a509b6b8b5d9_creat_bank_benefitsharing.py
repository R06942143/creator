"""creat Bank&BenefitSharing

Revision ID: a509b6b8b5d9
Revises: c18e926e95b7
Create Date: 2021-11-25 13:57:15.704870

"""
from alembic import op
import sqlalchemy as sa
import uuid
import datetime

from sqlalchemy.sql.schema import ForeignKey


# revision identifiers, used by Alembic.
revision = 'a509b6b8b5d9'
down_revision = 'c18e926e95b7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'bank',
        sa.Column(
            'id', sa.String(36), primary_key=True,
            default=str(uuid.uuid4()), nullable=False),
        sa.Column(
            'created_at', sa.types.DateTime(timezone=True),
            default=datetime.datetime.now(), nullable=False),
        sa.Column(
            'updated_at', sa.types.DateTime(timezone=True),
            default=datetime.datetime.now(), nullable=False),
        sa.Column('account', sa.String(50), nullable=False),
        sa.Column(
            'creator_id', sa.String(36),
            ForeignKey('creator.id', ondelete='CASCADE'), nullable=False)
    )
    op.create_table(
        'benefitsharing',
        sa.Column(
            'id', sa.String(36), primary_key=True,
            default=str(uuid.uuid4()), nullable=False),
        sa.Column(
            'created_at', sa.types.DateTime(timezone=True),
            default=datetime.datetime.now(), nullable=False),
        sa.Column(
            'updated_at', sa.types.DateTime(timezone=True),
            default=datetime.datetime.now(), nullable=False),
        sa.Column('amount', sa.Float(10), nullable=False),
        sa.Column('is_paid', sa.Boolean, nullable=False, default=False),
        sa.Column(
            'bank_id', sa.String(36),
            ForeignKey('bank.id', ondelete='CASCADE'), nullable=False)
    )


def downgrade():
    op.drop_table('benefitsharing')
    op.drop_table('bank')
    # pass