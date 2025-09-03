#!/bin/bash
# Build script for Vercel deployment

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations (if DATABASE_URL is set)
if [ ! -z "$DATABASE_URL" ]; then
    python manage.py migrate
fi
