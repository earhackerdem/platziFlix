"""
Models package for Platziflix platform

This module imports all SQLAlchemy models to ensure they are registered
with the Base.metadata for Alembic migrations.
"""

from .teacher import Teacher, course_teacher
from .course import Course
from .lesson import Lesson

# Export all models for easy importing
__all__ = [
    "Teacher",
    "Course", 
    "Lesson",
    "course_teacher"
] 