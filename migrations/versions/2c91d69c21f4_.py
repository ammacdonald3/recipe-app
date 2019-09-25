"""empty message

Revision ID: 2c91d69c21f4
Revises: 8e81852be74d
Create Date: 2019-09-24 21:40:58.048416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c91d69c21f4'
down_revision = '8e81852be74d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('diet_gluten', sa.String(), nullable=True))
    op.add_column('recipe', sa.Column('diet_vegan', sa.String(), nullable=True))
    op.add_column('recipe', sa.Column('diet_vegetarian', sa.String(), nullable=True))
    op.add_column('recipe', sa.Column('meal_time', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe', 'meal_time')
    op.drop_column('recipe', 'diet_vegetarian')
    op.drop_column('recipe', 'diet_vegan')
    op.drop_column('recipe', 'diet_gluten')
    # ### end Alembic commands ###
