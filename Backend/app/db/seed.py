"""
Seed data for Platziflix platform
Populates the database with sample data for development and testing
"""

from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime, timedelta

# Imports from our models
from .base import SessionLocal, Base
from .models import Teacher, Course, Lesson, course_teacher

def create_sample_teachers(db: Session) -> dict:
    """Create sample teachers and return them in a dictionary"""
    teachers_data = [
        {
            "name": "Juan Pérez",
            "email": "juan.perez@platziflix.com"
        },
        {
            "name": "María González",
            "email": "maria.gonzalez@platziflix.com"
        },
        {
            "name": "Carlos Rodríguez",
            "email": "carlos.rodriguez@platziflix.com"
        },
        {
            "name": "Ana Martínez",
            "email": "ana.martinez@platziflix.com"
        },
        {
            "name": "Pedro Sánchez",
            "email": "pedro.sanchez@platziflix.com"
        },
        {
            "name": "Laura López",
            "email": "laura.lopez@platziflix.com"
        },
        {
            "name": "Diego Hernández",
            "email": "diego.hernandez@platziflix.com"
        }
    ]
    
    teachers = {}
    for teacher_data in teachers_data:
        teacher = Teacher(**teacher_data)
        db.add(teacher)
        teachers[teacher_data["name"]] = teacher
    
    db.commit()
    print(f"✅ Created {len(teachers)} teachers")
    return teachers

def create_sample_courses(db: Session, teachers: dict) -> dict:
    """Create sample courses and return them in a dictionary"""
    courses_data = [
        {
            "name": "Curso de React",
            "description": "Aprende React desde cero hasta convertirte en un experto. Cubrimos hooks, context, routing y más.",
            "thumbnail": "https://via.placeholder.com/300x200/61DAFB/000000?text=React",
            "slug": "curso-de-react",
            "teachers": ["Juan Pérez", "María González"]
        },
        {
            "name": "Curso de Python",
            "description": "Domina Python desde los fundamentos hasta programación avanzada. Incluye Django y Flask.",
            "thumbnail": "https://via.placeholder.com/300x200/3776AB/FFFFFF?text=Python",
            "slug": "curso-de-python",
            "teachers": ["Carlos Rodríguez", "Ana Martínez"]
        },
        {
            "name": "Curso de JavaScript",
            "description": "JavaScript moderno: ES6+, async/await, DOM manipulation, APIs y más.",
            "thumbnail": "https://via.placeholder.com/300x200/F7DF1E/000000?text=JavaScript",
            "slug": "curso-de-javascript",
            "teachers": ["Juan Pérez", "Pedro Sánchez"]
        },
        {
            "name": "Curso de Next.js",
            "description": "Aprende Next.js para crear aplicaciones web modernas con React y SSR.",
            "thumbnail": "https://via.placeholder.com/300x200/000000/FFFFFF?text=Next.js",
            "slug": "curso-de-nextjs",
            "teachers": ["María González", "Laura López"]
        },
        {
            "name": "Curso de Node.js",
            "description": "Desarrollo backend con Node.js: APIs REST, Express, MongoDB y más.",
            "thumbnail": "https://via.placeholder.com/300x200/339933/FFFFFF?text=Node.js",
            "slug": "curso-de-nodejs",
            "teachers": ["Diego Hernández", "Pedro Sánchez"]
        },
        {
            "name": "Curso de TypeScript",
            "description": "TypeScript para desarrolladores JavaScript: tipado estático, interfaces y más.",
            "thumbnail": "https://via.placeholder.com/300x200/3178C6/FFFFFF?text=TypeScript",
            "slug": "curso-de-typescript",
            "teachers": ["Laura López", "Ana Martínez"]
        },
        {
            "name": "Curso de Vue.js",
            "description": "Vue.js 3: Composition API, Vuex, Vue Router y desarrollo de SPAs.",
            "thumbnail": "https://via.placeholder.com/300x200/4FC08D/FFFFFF?text=Vue.js",
            "slug": "curso-de-vuejs",
            "teachers": ["Carlos Rodríguez", "Diego Hernández"]
        }
    ]
    
    courses = {}
    for course_data in courses_data:
        # Separate teachers from course data
        teacher_names = course_data.pop("teachers")
        
        # Create course
        course = Course(**course_data)
        db.add(course)
        db.flush()  # Get the course ID
        
        # Add teachers to course
        for teacher_name in teacher_names:
            if teacher_name in teachers:
                course.teachers.append(teachers[teacher_name])
        
        courses[course_data["slug"]] = course
    
    db.commit()
    print(f"✅ Created {len(courses)} courses")
    return courses

def create_sample_lessons(db: Session, courses: dict) -> None:
    """Create sample lessons for each course"""
    lessons_data = {
        "curso-de-react": [
            {
                "name": "Introducción a React",
                "description": "Qué es React, por qué usarlo y configuración del entorno.",
                "slug": "introduccion-react",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Componentes y JSX",
                "description": "Creación de componentes y sintaxis JSX.",
                "slug": "componentes-jsx",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Props y State",
                "description": "Manejo de props y estado en React.",
                "slug": "props-state",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Hooks: useState y useEffect",
                "description": "Hooks fundamentales para el manejo de estado y efectos.",
                "slug": "hooks-usestate-useeffect",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "React Router",
                "description": "Navegación en aplicaciones React con React Router.",
                "slug": "react-router",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            }
        ],
        "curso-de-python": [
            {
                "name": "Fundamentos de Python",
                "description": "Variables, tipos de datos y operadores básicos.",
                "slug": "fundamentos-python",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Estructuras de Control",
                "description": "Condicionales, bucles y manejo de flujo.",
                "slug": "estructuras-control",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Funciones y Módulos",
                "description": "Definición de funciones y organización en módulos.",
                "slug": "funciones-modulos",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Programación Orientada a Objetos",
                "description": "Clases, objetos, herencia y polimorfismo.",
                "slug": "poo-python",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            }
        ],
        "curso-de-javascript": [
            {
                "name": "JavaScript Básico",
                "description": "Variables, tipos de datos y operadores.",
                "slug": "javascript-basico",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Funciones y Scope",
                "description": "Declaración de funciones y ámbito de variables.",
                "slug": "funciones-scope",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "DOM Manipulation",
                "description": "Manipulación del DOM con JavaScript.",
                "slug": "dom-manipulation",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Async/Await y Promises",
                "description": "Programación asíncrona en JavaScript.",
                "slug": "async-await-promises",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            }
        ],
        "curso-de-nextjs": [
            {
                "name": "Introducción a Next.js",
                "description": "Qué es Next.js y sus ventajas sobre React.",
                "slug": "introduccion-nextjs",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Routing y Pages",
                "description": "Sistema de routing automático de Next.js.",
                "slug": "routing-pages",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Server Side Rendering",
                "description": "SSR y generación estática con Next.js.",
                "slug": "server-side-rendering",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            }
        ],
        "curso-de-nodejs": [
            {
                "name": "Introducción a Node.js",
                "description": "Qué es Node.js y configuración del entorno.",
                "slug": "introduccion-nodejs",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Express.js Framework",
                "description": "Creación de APIs REST con Express.js.",
                "slug": "expressjs-framework",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Base de Datos con MongoDB",
                "description": "Integración con MongoDB y Mongoose.",
                "slug": "mongodb-mongoose",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            }
        ],
        "curso-de-typescript": [
            {
                "name": "Fundamentos de TypeScript",
                "description": "Tipado estático y configuración de TypeScript.",
                "slug": "fundamentos-typescript",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Interfaces y Types",
                "description": "Definición de interfaces y tipos personalizados.",
                "slug": "interfaces-types",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Generics y Decorators",
                "description": "Conceptos avanzados de TypeScript.",
                "slug": "generics-decorators",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            }
        ],
        "curso-de-vuejs": [
            {
                "name": "Introducción a Vue.js",
                "description": "Conceptos básicos y configuración de Vue.js.",
                "slug": "introduccion-vuejs",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Componentes Vue",
                "description": "Creación y comunicación entre componentes.",
                "slug": "componentes-vue",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "name": "Vuex State Management",
                "description": "Manejo de estado global con Vuex.",
                "slug": "vuex-state-management",
                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            }
        ]
    }
    
    lesson_count = 0
    for course_slug, course_lessons in lessons_data.items():
        if course_slug in courses:
            course = courses[course_slug]
            for lesson_data in course_lessons:
                lesson = Lesson(
                    course_id=course.id,
                    **lesson_data
                )
                db.add(lesson)
                lesson_count += 1
    
    db.commit()
    print(f"✅ Created {lesson_count} lessons")

def clear_existing_data(db: Session) -> None:
    """Clear existing data from the database"""
    print("🧹 Clearing existing data...")
    
    # Delete in reverse order of dependencies
    db.execute(text("DELETE FROM course_teacher"))
    db.query(Lesson).delete()
    db.query(Course).delete()
    db.query(Teacher).delete()
    
    db.commit()
    print("✅ Existing data cleared")

def seed_database() -> None:
    """Main function to seed the database"""
    print("🌱 Starting database seeding...")
    
    # Create database session
    db = SessionLocal()
    
    try:
        # Clear existing data
        clear_existing_data(db)
        
        # Create sample data
        teachers = create_sample_teachers(db)
        courses = create_sample_courses(db, teachers)
        create_sample_lessons(db, courses)
        
        print("🎉 Database seeding completed successfully!")
        
        # Print summary
        teacher_count = db.query(Teacher).count()
        course_count = db.query(Course).count()
        lesson_count = db.query(Lesson).count()
        
        print(f"📊 Summary:")
        print(f"   • Teachers: {teacher_count}")
        print(f"   • Courses: {course_count}")
        print(f"   • Lessons: {lesson_count}")
        
    except Exception as e:
        print(f"❌ Error during seeding: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed_database() 