#!/bin/sh

echo "started"
python manage.py makemigrations app
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuserwithpassword \
        --username omarmohamed \
        --password enter1234 \
        --email omarmohamed@example.org \
        --preserve

gunicorn --config gunicorn-cfg.py --reload project.wsgi