release: python src/manage.py migrate
web: gunicorn --chdir src payinv.wsgi:application
