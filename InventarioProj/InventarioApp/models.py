from django.db import models

# Create your models here.


class Inventario(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, serialize=False)
    articulo = models.CharField(max_length=255)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'Artículo: {self.articulo} ({self.cantidad})'
