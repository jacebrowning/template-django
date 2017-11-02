import os

import dj_database_url

from .base import *

BASE_NAME = os.environ['HEROKU_APP_NAME']
BASE_DOMAIN = f"{BASE_NAME}.com"
BASE_URL = f"https://{BASE_DOMAIN}"

###############################################################################
# Core

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    'localhost',
    # TODO: Remove this line and add your custom domain
    '.herokuapp.com',
]

###############################################################################
# Databases

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

###############################################################################
# Static files

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
