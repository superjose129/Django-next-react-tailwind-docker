from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "ioasdhjojasdiofjo"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    "django_extensions",
]
