from django.shortcuts import render
from .models import Inventario


# Create your views here.


def home(request):
    inventarioV = Inventario.objects.all()
    return render(request, 'gestionInv.html', {'inventario': inventarioV})
