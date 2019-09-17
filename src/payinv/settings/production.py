"""
    Settings for production enviroment
"""
from .base import *
import os

ALLOWED_HOSTS = ['.boxtub.com']
DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Emails settings
ADMINS = [('Rodrigo Ramirez', 'a@rodrigoramirez.com')]
EMAIL_SUBJECT_PREFIX = '[SP Admin] '
DEFAULT_FROM_EMAIL = 'a@rodrigoramirez.com'
