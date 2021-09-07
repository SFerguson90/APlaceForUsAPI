"""empty message

Revision ID: 8250d5ec7b49
Revises: 5136862763a0
Create Date: 2021-09-07 02:42:40.141659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8250d5ec7b49'
down_revision = '5136862763a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar_image', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'avatar_image')
    # ### end Alembic commands ###
