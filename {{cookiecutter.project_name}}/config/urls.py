from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import redirect


def append_slash_and_redirect(request):
    assert not request.path.endswith('/')
    return redirect(request.path + '/', permanent=True)


urlpatterns = [
    url('^(?:api|admin).*[^/]$', append_slash_and_redirect),

    url('^api/', include('{{cookiecutter.project_name}}.api.urls')),

    url('^admin/', admin.site.urls),
    url('^grappelli/', include('grappelli.urls')),
]
