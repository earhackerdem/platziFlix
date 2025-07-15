"""Create initial tables

Revision ID: 04619eb01c8d
Revises: 
Create Date: 2025-07-14 22:30:25.445327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04619eb01c8d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False, unique=True, index=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.Column('deleted_at', sa.DateTime, nullable=True),
    )
    
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('thumbnail', sa.String(500), nullable=False),
        sa.Column('slug', sa.String(255), nullable=False, unique=True, index=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.Column('deleted_at', sa.DateTime, nullable=True),
    )
    
    # Create classes table
    op.create_table(
        'classes',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('slug', sa.String(255), nullable=False, index=True),
        sa.Column('video_url', sa.String(500), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.Column('deleted_at', sa.DateTime, nullable=True),
    )
    
    # Create course_teacher association table
    op.create_table(
        'course_teacher',
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id', ondelete='CASCADE'), primary_key=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Drop tables in reverse order
    op.drop_table('course_teacher')
    op.drop_table('classes')
    op.drop_table('courses')
    op.drop_table('teachers')
