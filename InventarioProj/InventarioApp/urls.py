from django.urls import path
from .views import home, registrarArt

urlpatterns = [
    path('', home),
    path('registrar', registrarArt)
]
