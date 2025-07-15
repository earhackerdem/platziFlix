.PHONY: start stop restart build logs clean help seed init-db

# Comando principal para iniciar el entorno de desarrollo
start:
	docker compose up -d

# Detener los contenedores
stop:
	docker compose down

# Reiniciar los contenedores
restart:
	docker compose restart

# Construir las imágenes
build:
	docker compose build

# Ver los logs de los contenedores
logs:
	docker compose logs -f

# Inicializar la base de datos (crear tablas y ejecutar seed)
init-db:
	docker compose run --rm db-init

# Ejecutar solo el seed (poblar con datos de ejemplo)
seed:
	docker compose run --rm api seed

# Limpiar contenedores, volúmenes e imágenes
clean:
	docker compose down -v --rmi all --remove-orphans

# Mostrar ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  make start    - Iniciar el entorno de desarrollo"
	@echo "  make stop     - Detener los contenedores"
	@echo "  make restart  - Reiniciar los contenedores"
	@echo "  make build    - Construir las imágenes"
	@echo "  make logs     - Ver logs de los contenedores"
	@echo "  make init-db  - Inicializar base de datos (crear tablas + seed)"
	@echo "  make seed     - Ejecutar solo el seed (poblar datos)"
	@echo "  make clean    - Limpiar contenedores y volúmenes"
	@echo "  make help     - Mostrar esta ayuda"

# Comando por defecto
.DEFAULT_GOAL := help 