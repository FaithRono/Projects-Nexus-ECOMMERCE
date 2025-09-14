#!/bin/sh

# Wait for PostgreSQL to be ready
./wait-for-postgres.sh

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the Django application
exec python manage.py runserver 0.0.0.0:8000