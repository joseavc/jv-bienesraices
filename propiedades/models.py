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
    imagen = models.ImageField(null=True, blank=True, upload_to="prop_img/")
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class ClienteComprador(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    mensaje = models.TextField(default="Hola, me interesa este inmueble que vi y quiero que me contacten. Gracias.")
    propiedad_interes = models.ForeignKey("Propiedad",null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre