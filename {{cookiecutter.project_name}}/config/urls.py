from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('api/', include('{{cookiecutter.project_name}}.api.urls')),

    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
]
