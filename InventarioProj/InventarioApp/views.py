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


def editarArt(request, codigo):
    inv = Inventario.objects.get(codigo=codigo)
    return render(request, 'editar.html', {'i': inv})


def editarInv(request):
    codigo = request.POST['txtCodigo']
    articulo = request.POST['txtArticulo']
    cantidad = request.POST['numCantidad']

    inv = Inventario.objects.get(codigo=codigo)
    inv.articulo = articulo
    inv.cantidad = cantidad
    inv.save()

    return redirect('/')


def eliminarArt(request, codigo):
    inv = Inventario.objects.get(codigo=codigo)
    inv.delete()

    return redirect('/')
