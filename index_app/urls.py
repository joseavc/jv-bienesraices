"""
URL's de Index App
"""

from django.urls import path
from .views import *

app_name = 'index'

urlpatterns = [
    path("", hola)
]
