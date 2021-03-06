"""empty message

Revision ID: ebba71946c05
Revises: 9dbce11e2688
Create Date: 2020-09-20 19:18:30.608455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebba71946c05'
down_revision = '9dbce11e2688'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('shopping_list_ingredient_id_fkey', 'shopping_list', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('shopping_list_ingredient_id_fkey', 'shopping_list', 'ingredient', ['ingredient_id'], ['ingredient_id'])
    # ### end Alembic commands ###
