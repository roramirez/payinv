import os
from payinv.utils import get_secret

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
THIS_DIR = os.path.dirname(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__))))
BASE_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('PAYINV_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customers',
    'sales',
    'invoices',
    'payments',
    'core',
    'utilities',
    'registration',
    'django_extensions',
    'django_filters',
    'django_tables2',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'payinv.urls'

WSGI_APPLICATION = 'payinv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.setdefault(
            'PAYINV_DATABASE_NAME',
            'payinv_{}'.format(get_secret('PAYINV_ENVIRONMENT', 'production'))),
        'USER': get_secret('PAYINV_DATABASE_USER', 'payinv'),
        'PASSWORD': get_secret('PAYINV_DATABASE_PASSWORD'),
        'HOST': os.environ.setdefault('PAYINV_DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.setdefault('PAYINV_DATABASE_PORT', '5432'),
        'TEST': {
            'NAME': 'payinv_test',
        },
    },
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #{
    #    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: E501
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa: E501
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa: E501
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa: E501
    #},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es_ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static-project"),
)


APP_NAME = 'PayInv'


LOCALE_PATHS = [
     os.path.join(BASE_DIR, 'locale')
]
