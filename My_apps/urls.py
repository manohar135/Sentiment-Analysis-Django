from django.contrib import admin
from django.urls import path
from My_apps.views import *

urlpatterns = [
    path('', index, name="index"),
]