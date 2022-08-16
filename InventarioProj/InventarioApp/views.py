from django.shortcuts import render, redirect
from .models import Inventario


# Create your views here.


def home(request):
    inventarioV = Inventario.objects.all()
    return render(request, 'gestionInv.html', {'inventario': inventarioV})


def registrarArt(request):
    codigo = request.POST['txtCodigo']
    articulo = request.POST['txtArticulo']
    cantidad = request.POST['txtCantidad']

    inv = Inventario.objects.create(codigo=codigo, articulo=articulo, cantidad=cantidad)
    return redirect('/')

