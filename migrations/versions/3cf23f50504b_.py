"""empty message

Revision ID: 3cf23f50504b
Revises: c8a519534163
Create Date: 2020-08-19 15:21:50.649341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cf23f50504b'
down_revision = 'c8a519534163'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('current_meal', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'current_meal', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'current_meal', type_='foreignkey')
    op.drop_column('current_meal', 'user_id')
    # ### end Alembic commands ###