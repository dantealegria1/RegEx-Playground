from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logic/', include('regex_logic.urls')),
    path('', include('regex_ui.urls')),
]
