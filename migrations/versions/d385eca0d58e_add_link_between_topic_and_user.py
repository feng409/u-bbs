"""add link between topic and user

Revision ID: d385eca0d58e
Revises: a7b608183801
Create Date: 2018-05-15 21:39:41.624199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd385eca0d58e'
down_revision = 'a7b608183801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topic', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'topic', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'topic', type_='foreignkey')
    op.drop_column('topic', 'user_id')
    # ### end Alembic commands ###