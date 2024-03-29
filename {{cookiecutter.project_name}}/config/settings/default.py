import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(CONFIG_ROOT)

ALLOW_DEBUG = False
TEST = False

###############################################################################
# Core

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    "debug_toolbar",

    'allauth',
    'allauth.account',
    'corsheaders',
    'django_extensions',
    'rest_framework',
    'drf_yasg',

    '{{cookiecutter.project_name}}.api',
    '{{cookiecutter.project_name}}.core',
    '{{cookiecutter.project_name}}.{{cookiecutter.first_app_name}}',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "bugsnag.django.middleware.BugsnagMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": ["templates", os.path.join(PROJECT_ROOT, "{{cookiecutter.project_name}}", "templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        "bugsnag": {
            "level": "CRITICAL",
            "class": "bugsnag.handlers.BugsnagHandler",
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        '{{cookiecutter.project_name}}': {
            'handlers': ['console', 'bugsnag'],
            'level': 'DEBUG',
        },
    }
}

SITE_ID = 1

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

###############################################################################
# Sessions

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 52

###############################################################################
# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Michigan'

USE_I18N = True

USE_TZ = True

###############################################################################
# Static files

STATICFILES_DIRS = [os.path.join(PROJECT_ROOT, "static")]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

###############################################################################
# CORS

CORS_ORIGIN_ALLOW_ALL = True

###############################################################################
# Django Debug Toolbar

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_COLLAPSED": True,
    "SHOW_TOOLBAR_CALLBACK": "{{cookiecutter.project_name}}.core.helpers.allow_debug",
}
