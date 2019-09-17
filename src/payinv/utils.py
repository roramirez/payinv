import os
from django.core.exceptions import ImproperlyConfigured


def get_secret(secret_name, default_value=None):
    """
    Get secret from docker secret file or environment variable.

    @secret_name (str): Is parsed as lowercase when requested as docker \
        secret and uppercase when requested as environment variable.
    @default_value (str)

    returns (str): secret contents
    """
    try:
        with open('/run/secrets/{}'.format(secret_name.lower())) as file:
            return file.read().splitlines()[0]
    except IOError:
        try:
            return os.environ[secret_name.upper()]
        except KeyError:
            if default_value is not None:
                return default_value
            else:
                error_msg = 'Secret {} is not defined, neither as environment'\
                            'variable nor system secret'.format(secret_name)
                raise ImproperlyConfigured(error_msg)
