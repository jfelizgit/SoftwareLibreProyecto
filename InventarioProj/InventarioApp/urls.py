from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('registrar', registrarArt),
    path('editar/<codigo>', editarArt),
    path('editarInv/', editarInv),
    path('eliminar/<codigo>', eliminarArt)
]
