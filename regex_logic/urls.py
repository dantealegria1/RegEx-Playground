from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    path('reverse/', views.reverse_string_logic, name='reverse_string_logic'),
    path('regex/', views.regex_generator, name='regex_generator'),
    path('testing/', views.regex_testing, name='regex_testing'),
    path('normal/', views.regex_normal, name='regex_normal'),
]
