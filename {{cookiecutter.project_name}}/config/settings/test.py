from .base import *


TEST = True

DEBUG = True

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{cookiecutter.project_name}}_test',
    }
}

DISABLE_DATABASE_SETUP = False
