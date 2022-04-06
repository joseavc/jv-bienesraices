"""
URL's de Captacion App
"""

from django.urls import path

from index_app.views import hola
from .views import *

app_name = 'captacion'

urlpatterns = [
    path("", crear_prospecto, name="crearprospecto"),
    path("sent", confirmacion, name="enviado"),
]