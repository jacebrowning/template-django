from django.urls import path

from . import views


urlpatterns = [
    path('', views.current_datetime),
]

app_name = '{{cookiecutter.first_app_name}}'
