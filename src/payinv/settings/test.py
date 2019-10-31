from .base import *
import logging

DEBUG = True


INSTALLED_APPS += ('nplusone.ext.django', )


MIDDLEWARE.append('nplusone.ext.django.NPlusOneMiddleware')

NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            },
    },
    'loggers': {
        'nplusone': {
            'handlers': ['console'],
            'level': 'WARN',
            },
    },
}
