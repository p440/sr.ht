"""Removed oauth and toxid integrations

Revision ID: d84cd253a05b
Revises: 2c27bce164d
Create Date: 2018-02-16 19:12:23.475863

"""

# revision identifiers, used by Alembic.
revision = 'd84cd253a05b'
down_revision = '2c27bce164d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'tox_id')
    op.drop_table('oauth_tokens')
    op.drop_table('oauth_clients')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('tox_id', sa.VARCHAR(length=76), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
