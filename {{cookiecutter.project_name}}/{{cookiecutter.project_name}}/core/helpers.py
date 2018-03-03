from django.conf import settings


def build_url(path):
    assert settings.BASE_URL
    assert path.startswith('/')
    return settings.BASE_URL + path
