# pylint: skip-file
"""Add goal and goalprogress table

Revision ID: 12a80f78ad0b
Revises:
Create Date: 2022-06-23 11:37:37.426515

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '12a80f78ad0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'goal',
        sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('current_value', sa.Float(), nullable=True),
        sa.Column('desired_value', sa.Float(), nullable=False),
        sa.Column('unit', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('is_starred', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('last_edited', sa.DateTime(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'goalprogress',
        sa.Column('current_value', sa.Float(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goalprogress')
    op.drop_table('goal')
    # ### end Alembic commands ###
