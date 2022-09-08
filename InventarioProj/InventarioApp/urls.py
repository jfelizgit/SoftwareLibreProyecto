from django.urls import path
from .views import *

urlpatterns = [
    path('inventApp', home, name='inventApp'),
    path('registrar', registrarArt),
    path('editar/<codigo>', editarArt),
    path('editarInv/', editarInv),
    path('eliminar/<codigo>', eliminarArt),
    path('', index, name='home'),
    path('about', about, name='about'),
]
