# 🌱 Sistema de Seed - Platziflix

## Descripción

El sistema de seed de Platziflix puebla automáticamente la base de datos con datos de ejemplo para desarrollo y testing. Se ejecuta automáticamente al iniciar los contenedores.

## 📊 Datos Incluidos

### Profesores (7)
- Juan Pérez (juan.perez@platziflix.com)
- María González (maria.gonzalez@platziflix.com)
- Carlos Rodríguez (carlos.rodriguez@platziflix.com)
- Ana Martínez (ana.martinez@platziflix.com)
- Pedro Sánchez (pedro.sanchez@platziflix.com)
- Laura López (laura.lopez@platziflix.com)
- Diego Hernández (diego.hernandez@platziflix.com)

### Cursos (7)
1. **Curso de React** - Juan Pérez, María González
2. **Curso de Python** - Carlos Rodríguez, Ana Martínez
3. **Curso de JavaScript** - Juan Pérez, Pedro Sánchez
4. **Curso de Next.js** - María González, Laura López
5. **Curso de Node.js** - Diego Hernández, Pedro Sánchez
6. **Curso de TypeScript** - Laura López, Ana Martínez
7. **Curso de Vue.js** - Carlos Rodríguez, Diego Hernández

### Lecciones (30+)
Cada curso incluye entre 3-5 lecciones con contenido educativo apropiado.

## 🚀 Uso Automático

### Inicialización Automática

```bash
# El seed se ejecuta automáticamente al iniciar
make start
```

**Proceso automático:**
1. Inicia PostgreSQL
2. Espera a que esté listo (healthcheck)
3. Ejecuta `db-init` que:
   - Crea las tablas
   - Ejecuta el seed
   - Pobla con datos de ejemplo
4. Inicia la API FastAPI

## 🔧 Uso Manual

### Comandos Disponibles

```bash
# Inicializar base de datos completa (tablas + seed)
make init-db

# Solo ejecutar seed (requiere tablas existentes)
make seed

# Usando docker-compose directamente
docker compose run --rm db-init        # Inicialización completa
docker compose run --rm api seed       # Solo seed
```

### Desde el Contenedor

```bash
# Entrar al contenedor
docker compose exec api bash

# Ejecutar seed manualmente
python app/seed_runner.py --confirm

# Solo limpiar datos
python app/seed_runner.py --clear-only
```

## 📋 Estructura del Seed

### Archivos Principales

- `app/db/seed.py` - Datos de ejemplo y funciones de seed
- `app/seed_runner.py` - Script ejecutor con opciones
- `app/init_db.py` - Inicialización completa de base de datos

### Funciones Clave

```python
# En seed.py
create_sample_teachers(db)   # Crea profesores
create_sample_courses(db)    # Crea cursos con profesores
create_sample_lessons(db)    # Crea lecciones por curso
clear_existing_data(db)      # Limpia datos existentes
seed_database()              # Función principal
```

## 🛠️ Personalización

### Agregar Nuevos Datos

1. **Editar `app/db/seed.py`**
2. **Modificar las listas de datos:**

```python
# Agregar nuevo profesor
teachers_data = [
    # ... profesores existentes
    {
        "name": "Nuevo Profesor",
        "email": "nuevo@platziflix.com"
    }
]

# Agregar nuevo curso
courses_data = [
    # ... cursos existentes
    {
        "name": "Nuevo Curso",
        "description": "Descripción del nuevo curso",
        "thumbnail": "https://via.placeholder.com/300x200",
        "slug": "nuevo-curso",
        "teachers": ["Nuevo Profesor"]
    }
]
```

3. **Reiniciar contenedores:**

```bash
make restart
```

### Modificar Comportamiento

```python
# En seed.py - Modificar función principal
def seed_database():
    # Personalizar proceso de seed
    teachers = create_sample_teachers(db)
    courses = create_sample_courses(db, teachers)
    create_sample_lessons(db, courses)
    
    # Agregar lógica personalizada aquí
```

## 🚨 Solución de Problemas

### Seed Falla

```bash
# Ver logs del servicio de inicialización
docker compose logs db-init

# Verificar estado de la base de datos
docker compose logs db

# Ejecutar manualmente
make init-db
```

### Datos Duplicados

```bash
# Limpiar y reiniciar
make clean
make start
```

### Problemas de Conexión

```bash
# Verificar variables de entorno
docker compose exec api env | grep DATABASE

# Probar conexión manual
docker compose exec api python -c "from app.db.base import engine; print(engine.url)"
```

## 📝 Verificación

### Comprobar Datos

```bash
# Ejecutar script de prueba
docker compose exec api python test_setup.py

# Conectar a PostgreSQL
docker compose exec db psql -U platziflix_user -d platziflix_db

# Consultas útiles
SELECT COUNT(*) FROM teachers;
SELECT COUNT(*) FROM courses;
SELECT COUNT(*) FROM lessons;
```

### Endpoints de Verificación

```bash
# Verificar API
curl http://localhost:8000/health

# Ver documentación
open http://localhost:8000/docs
```

## 🔄 Flujo de Desarrollo

1. **Desarrollo inicial**: `make start` (seed automático)
2. **Cambios en seed**: Editar `seed.py` → `make restart`
3. **Solo repoblar**: `make seed`
4. **Limpiar todo**: `make clean` → `make start`

## 📈 Rendimiento

- **Tiempo de seed**: ~5-10 segundos
- **Registros creados**: ~50 registros totales
- **Memoria**: Mínima durante el proceso
- **Tiempo de inicialización**: ~30 segundos (incluyendo PostgreSQL)

## 🎯 Mejores Prácticas

1. **No modificar en producción**: Solo para desarrollo
2. **Backup antes de cambios**: `make clean` elimina todo
3. **Usar `--confirm`**: Para ejecución automática
4. **Verificar logs**: Siempre revisar salida del seed
5. **Probar cambios**: Usar `test_setup.py` para verificar 