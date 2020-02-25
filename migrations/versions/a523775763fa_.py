"""empty message

Revision ID: a523775763fa
Revises: c24ac2a54834
Create Date: 2020-01-29 09:55:29.874317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a523775763fa'
down_revision = 'c24ac2a54834'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('studentname', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'student', ['studentname'])
    op.drop_column('student', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('username', sa.VARCHAR(length=50), nullable=True))
    op.drop_constraint(None, 'student', type_='unique')
    op.drop_column('student', 'studentname')
    # ### end Alembic commands ###
