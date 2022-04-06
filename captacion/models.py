from django.db import models

class Propiedad(models.Model):
    """Modelo de Propiedad para la app captacion"""
    nombre_dueno = models.CharField(max_length=50)
    municipio = models.CharField(max_length=10)
    estado = models.TextField(blank=False, default="")
    tipo_credito = models.CharField(max_length=10)
    saldo = models.CharField(max_length=20, blank=True)
    nss = models.IntegerField(blank=True)
    whatsapp = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_dueno
    
