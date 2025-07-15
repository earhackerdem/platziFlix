"""
Teacher model for Platziflix platform
"""

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from typing import Optional

from ..base import Base, TimestampMixin

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
    
    def to_dict(self):
        """Convert teacher to dictionary for API responses"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        } 