from django.contrib import admin

# Register your models here.
from .models import Inventario


class FechaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')


admin.site.register(Inventario, FechaAdmin)
