# regex_ui/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Suponiendo que hay una vista llamada index
    path('reverse/', views.reverse_string_ui, name='reverse'),
    path('regex/', views.regex_generator_ui, name='regex'),
    path('testing/', views.regex_testing_ui, name='testing'),
    path('normal/', views.regex_normal_ui, name='normal'),
    path('', views.index, name='index'),
    path('info/',views.info, name='info')
]
