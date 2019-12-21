import os
import urllib

import dj_database_url

from .default import *


BASE_NAME = os.environ['HEROKU_APP_NAME']
BASE_DOMAIN = f"{BASE_NAME}.com"
BASE_URL = f"https://{BASE_DOMAIN}"

###############################################################################
# Core

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    '.herokuapp.com',  # TODO: Remove this line and add your custom domain
]

###############################################################################
# Databases

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

###############################################################################
# Caches

_redis = urllib.parse.urlparse(os.environ['REDIS_URL'])
CACHES = {
    'default': {
         'BACKEND': 'redis_cache.RedisCache',
         'LOCATION': f"{_redis.hostname}:{_redis.port}",
         'OPTIONS': {
             'PASSWORD': _redis.password,
             'DB': 0,
         },
    },
}

###############################################################################
# Authentication

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

###############################################################################
# Static files

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
