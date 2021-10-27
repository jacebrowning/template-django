from django.urls import include, path
from django.conf import settings

from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Root

root = routers.DefaultRouter()


# App: {{cookiecutter.first_app_name}}

# root.register(...)


# URLs

schema_view = get_schema_view(
    openapi.Info(
        title="{{cookiecutter.project_name}}",
        default_version='0',
        description="The API for {{cookiecutter.project_name}}.",
    ),
    url=settings.BASE_URL,
)

urlpatterns = [
    path('', include(root.urls)),

    path('client/', include('rest_framework.urls')),

    path('docs/', schema_view.with_ui('swagger')),
]
