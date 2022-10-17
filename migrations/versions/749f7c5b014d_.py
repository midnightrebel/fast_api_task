"""empty message

Revision ID: 749f7c5b014d
Revises: 942376187f4f
Create Date: 2022-10-17 12:21:42.020928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '749f7c5b014d'
down_revision = '942376187f4f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['Goods.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('category')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='category_pkey'),
    sa.UniqueConstraint('name', name='category_name_key')
    )
    op.drop_table('Goods')
    op.drop_table('Category')
    # ### end Alembic commands ###