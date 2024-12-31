from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    path('reverse/', views.reverse_string_logic, name='reverse_string_logic')
]
