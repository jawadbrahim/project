"""user

Revision ID: 870084f411f8
Revises: d9dcb5b4ab78
Create Date: 2024-09-10 09:51:24.178066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '870084f411f8'
down_revision = 'd9dcb5b4ab78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('token', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.UUID(), nullable=True))
        batch_op.drop_constraint('token_qa_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.drop_column('qa_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('token', schema=None) as batch_op:
        batch_op.add_column(sa.Column('qa_id', sa.UUID(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('token_qa_id_fkey', 'qa', ['qa_id'], ['id'])
        batch_op.drop_column('user_id')

    op.drop_table('user')
    # ### end Alembic commands ###