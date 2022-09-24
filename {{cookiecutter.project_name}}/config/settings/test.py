# mypy: ignore-errors

import bugsnag

from .default import *


# BASE_NAME and BASE_DOMAIN are intentionally unset
# None of the commands that rely on these values should run during tests
BASE_URL = "http://example.com"

###############################################################################
# Core

TEST = True
DEBUG = True
SECRET_KEY = 'test'

LOGGING['loggers']['{{cookiecutter.project_name}}']['level'] = 'DEBUG'

###############################################################################
# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{cookiecutter.project_name}}',  # automatically prefixed with "test_"
        'HOST': '127.0.0.1',
    }
}

###############################################################################
# Caches

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(PROJECT_ROOT, ".cache/django"),
    }
}

###############################################################################
# Bugsnag

bugsnag.configure(release_stage="test")

LOGGING["loggers"]["{{cookiecutter.project_name}}"]['handlers'].remove("bugsnag")
