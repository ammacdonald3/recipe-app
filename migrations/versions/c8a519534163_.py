"""empty message

Revision ID: c8a519534163
Revises: 0a127a8208c1
Create Date: 2020-08-18 21:55:22.681650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8a519534163'
down_revision = '0a127a8208c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ingredient', 'ingredient_qty')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ingredient', sa.Column('ingredient_qty', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
