# syntax=docker/dockerfile:1

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install system deps for psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency file and install
COPY walletsite/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project
COPY walletsite/ /app/

# Environment
ENV DJANGO_SETTINGS_MODULE=config.settings \
    PORT=8000

EXPOSE 8000

# Run with Gunicorn (collectstatic/migrate should be done by platform hooks or entrypoint)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
