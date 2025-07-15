# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install uv for dependency management
RUN pip install uv

# Copy dependency files and README
COPY pyproject.toml uv.lock README.md ./

# Install dependencies
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"
RUN uv sync --frozen

# Copy application code
COPY app/ ./app/
COPY ./specs ./specs

# Create entrypoint script
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
# Check if we should run database initialization\n\
if [ "$1" = "init-db" ]; then\n\
    echo "Running database initialization..."\n\
    python app/init_db.py\n\
    exit 0\n\
fi\n\
\n\
# Check if we should run only the seed\n\
if [ "$1" = "seed" ]; then\n\
    echo "Running database seed..."\n\
    python app/seed_runner.py --confirm\n\
    exit 0\n\
fi\n\
\n\
# Default: run the main application\n\
exec uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload\n\
' > /entrypoint.sh && chmod +x /entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Use the entrypoint script
ENTRYPOINT ["/entrypoint.sh"] 