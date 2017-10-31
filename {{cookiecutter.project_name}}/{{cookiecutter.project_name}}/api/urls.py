from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view


# Root

root = routers.DefaultRouter()


# App: {{cookiecutter.first_app_name}}

# root.register(...)


# URLs

urlpatterns = [
    url('^', include(root.urls)),

    url('^client/', include('rest_framework.urls')),

    url('^docs/', get_swagger_view(title="{{cookiecutter.project_name}} API")),
]
