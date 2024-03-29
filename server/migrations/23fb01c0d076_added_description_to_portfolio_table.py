"""added description to Portfolio table

Revision ID: 23fb01c0d076
Revises: 94b2e369fd68
Create Date: 2023-07-25 14:40:36.465506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23fb01c0d076'
down_revision = '94b2e369fd68'
branch_labels = ()
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolio', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('portfolio', 'description')
    # ### end Alembic commands ###
