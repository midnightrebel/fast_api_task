"""baseline

Revision ID: 8585d55e9de6
Revises: 
Create Date: 2022-10-17 12:12:39.315719

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '942376187f4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'category',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('count', sa.Integer()))


def downgrade() -> None:
    op.drop_table('category')
