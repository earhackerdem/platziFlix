"""Rename classes table to lessons

Revision ID: e27116ec238a
Revises: 04619eb01c8d
Create Date: 2025-07-14 23:26:59.264964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e27116ec238a'
down_revision: Union[str, Sequence[str], None] = '04619eb01c8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Rename table from 'classes' to 'lessons'
    op.rename_table('classes', 'lessons')


def downgrade() -> None:
    """Downgrade schema."""
    # Rename table back from 'lessons' to 'classes'
    op.rename_table('lessons', 'classes')
