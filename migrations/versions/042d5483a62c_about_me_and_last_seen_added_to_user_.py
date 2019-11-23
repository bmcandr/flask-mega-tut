"""about_me and last_seen added to user model

Revision ID: 042d5483a62c
Revises: d5fff4839342
Create Date: 2019-11-23 13:03:46.220488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '042d5483a62c'
down_revision = 'd5fff4839342'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
