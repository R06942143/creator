"""fist commit

Revision ID: c18e926e95b7
Revises:
Create Date: 2021-11-25 11:40:39.389660

"""
from alembic import op
import sqlalchemy as sa
import uuid
import datetime
from sqlalchemy.dialects.postgresql.base import BIT
from sqlalchemy.sql.schema import Column, ForeignKey, ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import String


# revision identifiers, used by Alembic.
revision = 'c18e926e95b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'creator',
        sa.Column(
            'id', sa.String(36), primary_key=True, default=str(uuid.uuid4())),
        sa.Column('account', sa.String(50), nullable=False, unique=True),
        sa.Column('pwd', sa.String(60), nullable=False),
        sa.Column('phone', sa.String(20), nullable=False, unique=True),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('is_active', sa.Boolean, default=True, nullable=False),
        sa.Column(
            'created_at', sa.types.DateTime(timezone=True),
            default=datetime.datetime.now(), nullable=False
        ),
        sa.Column(
            'updated_at', sa.types.DateTime(timezone=True),
            default=datetime.datetime.now(), nullable=False
        ),
        sa.Column('nick_name', sa.String(50)),
        sa.Column('brief_introduction', sa.TEXT),
        sa.Column('work_experience', sa.TEXT),
        sa.Column('case_type', sa.String(300))
    )
    op.create_table(
        'link',
        sa.Column(
            'id', sa.String(36), primary_key=True, default=str(uuid.uuid4())),
        sa.Column(
            'created_at', sa.types.DateTime(timezone=True),
            default=datetime.datetime.now(), nullable=False),
        sa.Column(
            'updated_at', sa.types.DateTime(timezone=True),
            default=datetime.datetime.now(), nullable=False),
        sa.Column('facebook', sa.String(200)),
        sa.Column('instagram', sa.String(200)),
        sa.Column('blog', sa.String(200)),
        sa.Column('youtube', sa.String(200)),
        sa.Column(
            'creator_id', sa.String(36),
            ForeignKey('creator.id', ondelete='CASCADE'), nullable=False
        )
    )



def downgrade():
    op.drop_table('link')
    op.drop_table('creator')
    # pass
