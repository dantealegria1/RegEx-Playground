# regex_ui/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Suponiendo que hay una vista llamada index
]
