# regex_ui/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Suponiendo que hay una vista llamada index
    path('reverse/', views.reverse_string_ui, name='reverse'),
    path('regex/', views.regex_generator_ui, name='regex')
]
