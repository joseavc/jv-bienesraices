"""
URL's de Propiedades App
"""

from django.urls import path
from .views import *

app_name = 'propiedades'

urlpatterns = [
    path("", hola)
]
