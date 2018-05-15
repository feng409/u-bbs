"""init commit

Revision ID: 96df02a3a63f
Revises: 
Create Date: 2018-05-15 14:12:23.447654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96df02a3a63f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.Column('created_time', sa.DECIMAL(), nullable=True),
    sa.Column('updated_time', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.Column('created_time', sa.DECIMAL(), nullable=True),
    sa.Column('updated_time', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('signature', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('topic')
    # ### end Alembic commands ###
