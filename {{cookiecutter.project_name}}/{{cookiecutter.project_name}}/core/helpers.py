from django.conf import settings


def build_url(path: str) -> str:
    assert settings.BASE_URL
    assert path.startswith('/')
    return settings.BASE_URL + path


def allow_debug(request) -> bool:
    if not settings.ALLOW_DEBUG:
        return False
    if request.GET.get("debug") == "false":
        return False
    if request.GET.get("debug"):
        return True
    return settings.DEBUG
