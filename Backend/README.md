# Platziflix Backend API

## 🎯 Descripción

Backend API para la plataforma de cursos online Platziflix. Construido con FastAPI, SQLAlchemy y PostgreSQL.

## 🚀 Características

- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para manejo de base de datos
- **PostgreSQL**: Base de datos relacional
- **Docker**: Contenedores para desarrollo
- **Seed automático**: Datos de ejemplo incluidos
- **Alembic**: Migraciones de base de datos

## 📋 Modelos de Datos

- **Teacher**: Profesores que imparten cursos
- **Course**: Cursos disponibles en la plataforma
- **Lesson**: Lecciones individuales de cada curso
- **Relación Many-to-Many**: Cursos pueden tener múltiples profesores

## 🛠️ Instalación y Uso

### Prerequisitos

- Docker y Docker Compose
- Make (opcional, para comandos simplificados)

### Inicio Rápido

```bash
# Clonar el repositorio
git clone <repository-url>
cd platziflix/Backend

# Iniciar el entorno completo (incluye seed automático)
make start

# O usando docker-compose directamente
docker compose up -d
```

### Comandos Disponibles

```bash
# Iniciar servicios
make start

# Detener servicios
make stop

# Ver logs
make logs

# Inicializar base de datos manualmente
make init-db

# Ejecutar solo seed (poblar datos)
make seed

# Limpiar todo
make clean

# Ver ayuda
make help
```

## 🌱 Sistema de Seed

El proyecto incluye un sistema de seed automático que se ejecuta al iniciar los contenedores:

### Datos de Ejemplo Incluidos

- **7 Profesores**: Juan Pérez, María González, Carlos Rodríguez, etc.
- **7 Cursos**: React, Python, JavaScript, Next.js, Node.js, TypeScript, Vue.js
- **30+ Lecciones**: Distribuidas entre los cursos

### Configuración Automática

1. **Al iniciar con `make start`**: La base de datos se inicializa automáticamente
2. **Servicio `db-init`**: Se ejecuta una vez y pobla la base de datos
3. **Servicio `api`**: Inicia solo después de que la base de datos esté lista

### Uso Manual

```bash
# Inicializar base de datos desde cero
make init-db

# Solo ejecutar seed (requiere tablas existentes)
make seed

# Ejecutar seed desde el contenedor
docker compose run --rm api seed
```

## 🔧 Configuración

### Variables de Entorno

```env
DATABASE_URL=postgresql://platziflix_user:platziflix_password@db:5432/platziflix_db
PROJECT_NAME=Platziflix
VERSION=1.0.0
```

### Estructura del Proyecto

```
Backend/
├── app/
│   ├── core/
│   │   └── config.py          # Configuración de la aplicación
│   ├── db/
│   │   ├── base.py            # Configuración de SQLAlchemy
│   │   ├── models.py          # Modelos de datos
│   │   └── seed.py            # Datos de ejemplo
│   ├── init_db.py             # Inicialización de base de datos
│   ├── seed_runner.py         # Ejecutor de seed
│   └── main.py                # Aplicación FastAPI
├── docker-compose.yml         # Configuración de servicios
├── Dockerfile                 # Imagen de la aplicación
├── Makefile                   # Comandos útiles
└── pyproject.toml             # Dependencias Python
```

## 📊 Endpoints API

### Información General

- `GET /`: Mensaje de bienvenida
- `GET /health`: Estado de la aplicación
- `GET /docs`: Documentación Swagger
- `GET /redoc`: Documentación ReDoc

## 🧪 Desarrollo

### Agregar Nuevos Datos al Seed

1. Editar `app/db/seed.py`
2. Modificar las funciones `create_sample_*`
3. Reiniciar los contenedores

### Ejecutar Migraciones

```bash
# Desde el contenedor
docker compose exec api alembic upgrade head

# Crear nueva migración
docker compose exec api alembic revision --autogenerate -m "Description"
```

## 🚨 Solución de Problemas

### Base de Datos No Disponible

Si el seed falla:

```bash
# Verificar estado de la base de datos
docker compose logs db

# Reiniciar servicios
make restart
```

### Limpiar y Reiniciar

```bash
# Limpiar completamente
make clean

# Reconstruir e iniciar
make build
make start
```

## 📝 Contribución

1. Fork el proyecto
2. Crear rama feature (`git checkout -b feature/amazing-feature`)
3. Commit cambios (`git commit -m 'Add amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abrir Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT.