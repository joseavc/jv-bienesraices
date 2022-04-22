"""Modelo de las Propiedades"""
from django.db import models

class Propiedad(models.Model):
    titulo = models.CharField(max_length=50)
    precio = models.IntegerField()
    colonia = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    descripcion = models.TextField(default="")
    recamaras = models.IntegerField()
    banos = models.FloatField()
    metros_construccion = models.IntegerField()
    metros_terreno = models.IntegerField()
    pisos = models.IntegerField()
    # imagen = models.ImageField(upload_to="")
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo