import logging

from django.conf import settings


log = logging.getLogger(__name__)


def build_url(path):
    assert settings.BASE_URL
    assert path.startswith('/')
    return settings.BASE_URL + path
