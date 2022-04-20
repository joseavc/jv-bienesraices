"""
URL's de Contacto App
"""

from django.urls import path
from .views import *

app_name = 'contacto'

urlpatterns = [
    path("", crear_cliente, name="contacto"),
    path("sent", confirmacion, name="enviado"),
]