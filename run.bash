#!/bin/bash

nohup celery -A CMP.celery worker -l INFO -E &
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
