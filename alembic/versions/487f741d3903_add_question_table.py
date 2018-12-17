"""add question table

Revision ID: 487f741d3903
Revises: 6046c7c7c022
Create Date: 2018-12-06 11:39:36.439290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '487f741d3903'
down_revision = '6046c7c7c022'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_type', sa.String(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('start_date', sa.String(), nullable=False),
    sa.Column('end_date', sa.String(), nullable=False),
    sa.Column('total_responses', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    # ### end Alembic commands ###