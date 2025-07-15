"""
Lesson model for Platziflix platform
Individual lessons within a course
"""

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from typing import Optional

from ..base import Base, TimestampMixin

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
    
    def to_dict(self, include_course: bool = False):
        """Convert lesson to dictionary for API responses"""
        data = {
            "id": self.id,
            "course_id": self.course_id,
            "name": self.name,
            "description": self.description,
            "slug": self.slug,
            "video_url": self.video_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        }
        
        if include_course and self.course:
            data["course"] = self.course.to_summary_dict()
            
        return data
    
    def to_summary_dict(self):
        """Convert lesson to summary dictionary for nested responses"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "slug": self.slug,
        } 