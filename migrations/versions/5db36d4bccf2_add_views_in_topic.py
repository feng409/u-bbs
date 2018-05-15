"""add views in Topic

Revision ID: 5db36d4bccf2
Revises: d385eca0d58e
Create Date: 2018-05-15 22:53:42.763554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5db36d4bccf2'
down_revision = 'd385eca0d58e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topic', sa.Column('views', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('topic', 'views')
    # ### end Alembic commands ###
