from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import api_home

urlpatterns = [
    path('', api_home),
]