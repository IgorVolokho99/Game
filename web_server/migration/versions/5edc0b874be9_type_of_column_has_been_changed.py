"""Type of column has been changed

Revision ID: 5edc0b874be9
Revises: e758b43b1e2f
Create Date: 2024-11-10 02:25:25.955529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5edc0b874be9'
down_revision: Union[str, None] = 'e758b43b1e2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
