#!/bin/sh

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate --no-input
gunicorn zzolab.wsgi -w 3 -b 0.0.0.0:8000
