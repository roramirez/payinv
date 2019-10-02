"""
    Settings for production enviroment
"""
from .base import *
import os

ALLOWED_HOSTS = ['mi.domain.com']
DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Emails settings
ADMINS = [('My Super Admin', 'admin@domain.com')]
EMAIL_SUBJECT_PREFIX = '[Payinv] '
DEFAULT_FROM_EMAIL = 'micontact@domain.com'
