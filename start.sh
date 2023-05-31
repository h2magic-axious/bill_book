#!/usr/bin/env bash

python manage.py migrate
python manage.py initial_admin

gunicorn bill_book.wsgi:application -b 0.0.0.0:80 \
  --workers 1 \
  --user=root \
  --log-level=info