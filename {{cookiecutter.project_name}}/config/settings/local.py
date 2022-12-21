# mypy: ignore-errors

import bugsnag
import dj_database_url

from .default import *  # pylint: disable=wildcard-import,unused-wildcard-import


BASE_NAME = BASE_DOMAIN = "localhost"
BASE_URL = f"http://{BASE_DOMAIN}:8000"

ALLOW_DEBUG = True

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
    'django_browser_reload',
]

MIDDLEWARE += [
    'django_browser_reload.middleware.BrowserReloadMiddleware',
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

###############################################################################
# Bugsnag

bugsnag.configure(release_stage="local")

LOGGING["loggers"]["{{cookiecutter.project_name}}"]['handlers'].remove("bugsnag")
