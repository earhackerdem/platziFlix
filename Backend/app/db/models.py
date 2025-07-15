"""
Unified models for Platziflix platform
All SQLAlchemy models in one file for better Alembic integration
"""

from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from typing import Optional, List

from .base import Base, TimestampMixin

# Tabla intermedia para la relación Many-to-Many entre Course y Teacher
course_teacher = Table(
    'course_teacher',
    Base.metadata,
    Column('course_id', Integer, ForeignKey('courses.id', ondelete='CASCADE'), primary_key=True),
    Column('teacher_id', Integer, ForeignKey('teachers.id', ondelete='CASCADE'), primary_key=True)
)

class Teacher(Base, TimestampMixin):
    """
    Teacher model representing instructors who teach courses
    """
    __tablename__ = 'teachers'
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Teacher information
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    
    # Relationships
    courses = relationship(
        "Course", 
        secondary=course_teacher,
        back_populates="teachers"
    )
    
    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"


class Course(Base, TimestampMixin):
    """
    Course model representing educational courses on the platform
    """
    __tablename__ = 'courses'
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Course information
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    thumbnail = Column(String(500), nullable=False)  # URL to course thumbnail
    slug = Column(String(255), unique=True, nullable=False, index=True)
    
    # Relationships
    teachers = relationship(
        "Teacher", 
        secondary=course_teacher,
        back_populates="courses"
    )
    
    lessons = relationship(
        "Lesson",
        back_populates="course",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', slug='{self.slug}')>"


class Lesson(Base, TimestampMixin):
    """
    Lesson model representing individual lessons within a course
    """
    __tablename__ = 'lessons'
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key to course
    course_id = Column(Integer, ForeignKey('courses.id', ondelete='CASCADE'), nullable=False, index=True)
    
    # Lesson information
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    slug = Column(String(255), nullable=False, index=True)
    video_url = Column(String(500), nullable=False)  # URL to video content
    
    # Relationships
    course = relationship("Course", back_populates="lessons")
    
    def __repr__(self):
        return f"<Lesson(id={self.id}, name='{self.name}', course_id={self.course_id})>" 