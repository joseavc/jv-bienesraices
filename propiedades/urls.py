"""
URL's de Propiedades App
"""

from django.urls import path
from .views import *

app_name = 'propiedades'

urlpatterns = [
    path("", lista_propiedades, name="lista_propiedades"),
    path("<int:pk>", ver_propiedad, name="ver_propiedad"),
]
