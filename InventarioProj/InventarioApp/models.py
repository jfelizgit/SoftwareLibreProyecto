from django.db import models
import os


# Create your models here.


class Inventario(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    codigo = models.CharField(primary_key=True, max_length=10, serialize=False)
    articulo = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(upload_to='inventario', null=True, blank=True)


    def __str__(self):
        return f'Artículo: {self.articulo} ({self.cantidad})'
