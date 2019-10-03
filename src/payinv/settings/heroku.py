"""
    Settings for Heroku deploy
    notes:
    You need add buildpacks for nodejs. This will using by bower
    Javascript and CSS dependencies

        $ heroku buildpacks:add --index 1 heroku/nodejs -a mi_app_name

    Environmet variables.
     `app_name`: Name of app on Heroku

        $ heroku config:set DISABLE_COLLECTSTATIC=0 -a mi_app_name
        $ heroku config:set DJANGO_SETTINGS_MODULE=payinv.settings.heroku -a mi_app_name
        $ heroku config:set PAYINV_ENVIRONMENT=production -a mi_app_name
        $ heroku config:set PAYINV_SECRET_KEY=MI_SECRET_KEY -a mi_app_name

    Or adding by web application https://dashboard.heroku.com/apps/app_name/settings

"""
from .base import *
import os

import django_heroku

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE.append(
    # Simplified static file serving.abs
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware'
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
