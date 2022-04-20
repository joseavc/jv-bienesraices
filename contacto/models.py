"""Contacto Models"""

from argparse import _MutuallyExclusiveGroup
from django.db import models

class Cliente(models.Model):
    """Prospecto Model"""
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    interes = models.CharField(max_length=10)
    mensaje = models.TextField(default="")
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


