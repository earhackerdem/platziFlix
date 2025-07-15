"""
Data Inspector for Platziflix Platform
Script to inspect and display seeded data in a readable format
"""

import sys
from pathlib import Path
from sqlalchemy.orm import Session

# Add current directory to Python path  
current_dir = Path(__file__).parent.parent
sys.path.insert(0, str(current_dir))

from db.base import SessionLocal
from db.models import Teacher, Course, Lesson

def inspect_teachers(db: Session) -> None:
    """Display all teachers"""
    print("👨‍🏫 TEACHERS")
    print("=" * 50)
    
    teachers = db.query(Teacher).all()
    for teacher in teachers:
        print(f"• {teacher.name} ({teacher.email})")
        courses = [course.name for course in teacher.courses]
        if courses:
            print(f"  📚 Courses: {', '.join(courses)}")
        print()

def inspect_courses(db: Session) -> None:
    """Display all courses with their details"""
    print("📚 COURSES")
    print("=" * 50)
    
    courses = db.query(Course).all()
    for course in courses:
        print(f"• {course.name}")
        print(f"  🔗 Slug: {course.slug}")
        print(f"  📝 Description: {course.description}")
        
        # Teachers
        teachers = [teacher.name for teacher in course.teachers]
        if teachers:
            print(f"  👨‍🏫 Teachers: {', '.join(teachers)}")
        
        # Lessons count
        lesson_count = len(course.lessons)
        print(f"  📖 Lessons: {lesson_count}")
        
        print()

def inspect_lessons(db: Session) -> None:
    """Display all lessons grouped by course"""
    print("📖 LESSONS")
    print("=" * 50)
    
    courses = db.query(Course).all()
    for course in courses:
        print(f"📚 {course.name}")
        print("-" * 30)
        
        for i, lesson in enumerate(course.lessons, 1):
            print(f"  {i}. {lesson.name}")
            print(f"     🔗 Slug: {lesson.slug}")
            print(f"     📝 {lesson.description}")
            print()

def show_statistics(db: Session) -> None:
    """Display database statistics"""
    print("📊 DATABASE STATISTICS")
    print("=" * 50)
    
    teacher_count = db.query(Teacher).count()
    course_count = db.query(Course).count()
    lesson_count = db.query(Lesson).count()
    
    print(f"👨‍🏫 Teachers: {teacher_count}")
    print(f"📚 Courses: {course_count}")
    print(f"📖 Lessons: {lesson_count}")
    
    # Average lessons per course
    avg_lessons = lesson_count / course_count if course_count > 0 else 0
    print(f"📈 Average lessons per course: {avg_lessons:.1f}")
    
    # Courses with most lessons
    courses_with_lessons = db.query(Course).all()
    if courses_with_lessons:
        most_lessons = max(courses_with_lessons, key=lambda c: len(c.lessons))
        print(f"🏆 Course with most lessons: {most_lessons.name} ({len(most_lessons.lessons)} lessons)")
    
    print()

def main():
    """Main function to inspect all data"""
    print("🔍 PLATZIFLIX DATA INSPECTOR")
    print("=" * 60)
    print()
    
    db = SessionLocal()
    
    try:
        show_statistics(db)
        inspect_teachers(db)
        inspect_courses(db)
        inspect_lessons(db)
        
        print("✅ Data inspection completed!")
        
    except Exception as e:
        print(f"❌ Error during inspection: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main() 