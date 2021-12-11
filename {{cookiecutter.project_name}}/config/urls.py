from django.contrib import admin
from django.urls import include, path
import debug_toolbar

from django.conf import settings

urlpatterns = [
    path('', include('{{cookiecutter.project_name}}.{{cookiecutter.first_app_name}}.urls', namespace='{{cookiecutter.first_app_name}}')),
    path('api/', include('{{cookiecutter.project_name}}.api.urls')),

    path('admin/', admin.site.urls),
]

if settings.ALLOW_DEBUG:
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
