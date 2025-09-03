# syntax=docker/dockerfile:1

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install system deps (libpq for psycopg2-binary runtime SSL)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy app files
COPY walletsite/ /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Collect static (safe if no storage backend)
RUN python manage.py collectstatic --noinput || true

# Environment
ENV DJANGO_SETTINGS_MODULE=config.settings \
    PORT=8000

EXPOSE 8000

# Start with migrations then gunicorn
CMD ["bash", "-lc", "python manage.py migrate --noinput || (sleep 5 && python manage.py migrate --noinput); gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers=1 --timeout 120 --log-file -"]
