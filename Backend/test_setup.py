#!/usr/bin/env python3
"""
Test script to verify database setup and seed data
"""

import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent / "app"
sys.path.insert(0, str(current_dir))

from db.base import SessionLocal
from db.models import Teacher, Course, Lesson

def test_database_setup():
    """Test that database is properly set up with seed data"""
    print("🧪 Testing database setup...")
    
    db = SessionLocal()
    
    try:
        # Test teachers
        teacher_count = db.query(Teacher).count()
        print(f"👨‍🏫 Teachers in database: {teacher_count}")
        
        # Test courses
        course_count = db.query(Course).count()
        print(f"📚 Courses in database: {course_count}")
        
        # Test lessons
        lesson_count = db.query(Lesson).count()
        print(f"🎓 Lessons in database: {lesson_count}")
        
        # Show first few records
        print("\n📋 Sample data:")
        
        # First teacher
        first_teacher = db.query(Teacher).first()
        if first_teacher:
            print(f"  • Teacher: {first_teacher.name} ({first_teacher.email})")
        
        # First course with its teachers
        first_course = db.query(Course).first()
        if first_course:
            teacher_names = [t.name for t in first_course.teachers]
            print(f"  • Course: {first_course.name} - Teachers: {', '.join(teacher_names)}")
        
        # First lesson
        first_lesson = db.query(Lesson).first()
        if first_lesson:
            print(f"  • Lesson: {first_lesson.name} (Course: {first_lesson.course.name})")
        
        # Verify expected counts
        expected_teachers = 7
        expected_courses = 7
        expected_lessons = 30  # Approximate
        
        print(f"\n✅ Database verification:")
        print(f"  • Teachers: {teacher_count}/{expected_teachers} {'✓' if teacher_count >= expected_teachers else '✗'}")
        print(f"  • Courses: {course_count}/{expected_courses} {'✓' if course_count >= expected_courses else '✗'}")
        print(f"  • Lessons: {lesson_count}/{expected_lessons} {'✓' if lesson_count >= expected_lessons else '✗'}")
        
        if teacher_count >= expected_teachers and course_count >= expected_courses and lesson_count >= expected_lessons:
            print("\n🎉 Database setup is working correctly!")
            return True
        else:
            print("\n❌ Database setup has issues!")
            return False
            
    except Exception as e:
        print(f"❌ Error testing database: {e}")
        return False
    finally:
        db.close()

if __name__ == "__main__":
    success = test_database_setup()
    sys.exit(0 if success else 1) 