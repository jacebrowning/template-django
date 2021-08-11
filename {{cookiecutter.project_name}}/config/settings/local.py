import dj_database_url

from .default import *


BASE_NAME = BASE_DOMAIN = "localhost"
BASE_URL = f"http://{BASE_DOMAIN}:8000"

###############################################################################
# Core

DEBUG = True
SECRET_KEY = 'dev'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.ngrok.io',
]

INSTALLED_APPS += [
    'livereload',
]

MIDDLEWARE += [
    'livereload.middleware.LiveReloadScript',
]

###############################################################################
# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{cookiecutter.project_name}}_dev',
        'HOST': '127.0.0.1',
    }
}

if "DATABASE_URL" in os.environ:
    DATABASES["default"] = dj_database_url.config()
