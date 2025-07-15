"""
Course model for Platziflix platform
"""

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from typing import Optional, List

from ..base import Base, TimestampMixin
from .teacher import course_teacher

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
    
    def to_dict(self, include_lessons: bool = False, include_teachers: bool = False):
        """Convert course to dictionary for API responses"""
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "thumbnail": self.thumbnail,
            "slug": self.slug,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        }
        
        if include_teachers:
            data["teachers"] = [teacher.to_dict() for teacher in self.teachers]
            
        if include_lessons:
            data["lessons"] = [lesson.to_dict() for lesson in self.lessons]
            
        return data
    
    def to_summary_dict(self):
        """Convert course to summary dictionary for list endpoints"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "thumbnail": self.thumbnail,
            "slug": self.slug,
        } 