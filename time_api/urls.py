# time_api/urls.py
from django.contrib import admin
from django.urls import path

from times.views import time_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/time/', time_api),
]