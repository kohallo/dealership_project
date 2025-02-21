#!/bin/sh

# Make migrations and migrate the database
echo "Making migrations and migrating the database. "
python manage.py makemigrations --noinput
python manage.py migrate --noinput
pyhton manage.py collectstatic --noinput
exec "$@"