"""empty message

Revision ID: b9eebb373aa3
Revises: 
Create Date: 2025-07-10 00:00:32.729002

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9eebb373aa3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
