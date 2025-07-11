# Platziflix

Plataforma online de cursos, cada curso tiene clases, descripciones y no hay mucho mas, eso es el inicio.

## Stacks

### Frontend
- Typescript
- CSS Modules
- SASS

### Mobile
- iOS
    - Swift
    - SwiftUI
- Android:
    - Kotlin
    - Jetpack Compose

### Backend 
- Python
- FastAPI
- PostgreSQL

## Contratos

### Entidades

1. Curso
2. Entidades
3. Profesor

### Contratos

- Cursos:
```json
{
    "id": 1,
    "name" : "Curso de React",
    "description" : "Clase 1",
    "thumbnail" : "https//via.placeholder.com/150",
    "slug" : "curso-de-react",
    "teacher_ids" : [1,2,3],
    "created_at" : "2021-01-01",
    "updated_at" : "2021-01-01",
    "deleted_at" : "2021-01-01"
}
```

- Clases:
```json
{
    "id": 1,
    "name" : "Curso de React",
    "description" : "Clase 1",
    "slug" : "clase-1",
    "video_url" : "www.youtube.com/watch/?v=df9ua13ed",
    "course_id" : 1,
    "created_at" : "2021-01-01",
    "updated_at" : "2021-01-01",
    "deleted_at" : "2021-01-01"
}
```

- Profesores:
```json
{
    "id": 1,
    "name" : "Curso de React",
    "email" : "john.doe@example.com",
    "created_at" : "2021-01-01",
    "updated_at" : "2021-01-01",
    "deleted_at" : "2021-01-01"
}
```

### Endpoints

- GET /courses -> Listar todos los cursos

```json
[
    {
    "id": 1,
    "name" : "Curso de React",
    "description" : "Clase 1",
    "thumbnail" : "https//via.placeholder.com/150",
    "slug" : "curso-de-react",
    }
]
```

- GET /courses/:slug -> Obtener un curso

```json
[
    {
    "id": 1,
    "name" : "Curso de React",
    "description" : "Clase 1",
    "thumbnail" : "https//via.placeholder.com/150",
    "slug" : "curso-de-react",
    "teacher_ids": [1,2,3],
    "classes" : [
        {
            "id" : 1,
            "name" : "Clase 1",
            "description" : "Clase 1",
            "slug" : "clase-1"
        }
    ]
    }
]
```

- GET /courses/:slug/classes/:id -> Obtener una clase
```json
{
    "id": 1,
    "name" : "Clase 1",
    "description" : "Clase 1",
    "slug" : "clase-1",
    "video_url" : "www.youtube.com/watch/?v=df9ua13ed",
    "created_at" : "2021-01-01",
    "updated_at" : "2021-01-01",
    "deleted_at" : "2021-01-01"
}
```
