"""a

Revision ID: cb7f205744a2
Revises: c214b7ebc27d
Create Date: 2024-09-08 10:44:15.331505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb7f205744a2'
down_revision = 'c214b7ebc27d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('token', schema=None) as batch_op:
        batch_op.add_column(sa.Column('auth_id', sa.UUID(), nullable=True))
        batch_op.create_foreign_key(None, 'auth', ['auth_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('token', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('auth_id')

    # ### end Alembic commands ###
