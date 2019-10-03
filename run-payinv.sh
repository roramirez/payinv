#!/bin/sh

python src/manage.py migrate
python src/manage.py check --deploy
python src/manage.py collectstatic --no-input
python src/manage.py compilemessages -l es

python src/manage.py runserver
