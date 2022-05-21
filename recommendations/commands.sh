#!/usr/bin/env bash
set -e

python manage.py migrate
python manage.py loaddata admin
python manage.py runserver 0.0.0.0:8000