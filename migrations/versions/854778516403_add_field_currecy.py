"""add field currecy

Revision ID: 854778516403
Revises: 2b792f766adc
Create Date: 2023-10-07 11:49:19.783636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '854778516403'
down_revision: Union[str, None] = '2b792f766adc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('currency', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'currency')
    # ### end Alembic commands ###
