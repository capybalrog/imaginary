"""Create index on images.is_active

Revision ID: 345a047f1fe9
Revises: 2e14df358ccd
Create Date: 2025-12-03 21:58:45.432715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '345a047f1fe9'
down_revision: Union[str, Sequence[str], None] = '2e14df358ccd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_index('ix_images_is_active', 'images', ['is_active'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('ix_images_is_active', table_name='images')
