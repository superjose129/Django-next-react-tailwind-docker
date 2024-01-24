import os

from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False

# White Noise configuration - http://whitenoise.evans.io/en/stable/django.html
INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])

# Must insert after SecurityMiddleware, which is first in settings/common.py
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

TEMPLATES[0]["DIRS"] = [os.path.join(BASE_DIR, "../", "react", "build")]

STATICFILES_DIRS = [os.path.join(BASE_DIR, "../", "react", "build", "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"
WHITENOISE_ROOT = os.path.join(BASE_DIR, "../", "react", "build", "root")
