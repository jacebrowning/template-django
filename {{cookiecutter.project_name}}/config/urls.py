from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('api/', include('{{cookiecutter.project_name}}.api.urls')),

    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
]
