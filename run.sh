#!/bin/bash

yes yes | python manage.py makemigrations && python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=12wqasxz python manage.py createsuperuser --noinput --email admin@admin.com
python manage.py fill_fake_in_db
python manage.py runserver 0.0.0.0:8000