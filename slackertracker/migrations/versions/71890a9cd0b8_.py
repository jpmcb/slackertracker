"""empty message

Revision ID: 71890a9cd0b8
Revises: 
Create Date: 2018-03-29 21:49:38.168767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71890a9cd0b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.String(length=32), nullable=False),
    sa.Column('slack_id', sa.String(length=32), nullable=False),
    sa.Column('display_name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slack_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###