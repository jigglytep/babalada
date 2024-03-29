"""updated investments transacted

Revision ID: f4d801513fba
Revises: 535be6be5d4d
Create Date: 2023-07-27 01:10:34.137943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4d801513fba'
down_revision = '535be6be5d4d'
branch_labels = ()
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('investment_transacted', sa.Column('portfolio_id', sa.Integer(), nullable=True))
    op.drop_constraint('investment_transacted_user_id_fkey', 'investment_transacted', type_='foreignkey')
    op.create_foreign_key(None, 'investment_transacted', 'portfolio', ['portfolio_id'], ['portfolioId'])
    op.drop_column('investment_transacted', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('investment_transacted', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'investment_transacted', type_='foreignkey')
    op.create_foreign_key('investment_transacted_user_id_fkey', 'investment_transacted', 'user', ['user_id'], ['id'])
    op.drop_column('investment_transacted', 'portfolio_id')
    # ### end Alembic commands ###
