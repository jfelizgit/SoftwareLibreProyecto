from django.shortcuts import render, redirect
from .models import Inventario
from django.contrib import messages


# Create your views here.


def home(request):
    inventarioV = Inventario.objects.all()
    messages.success(request, 'Registro listado')
    return render(request, 'gestionInv.html', {'inventario': inventarioV})


def registrarArt(request):
    codigo = request.POST['txtCodigo']
    articulo = request.POST['txtArticulo']
    cantidad = request.POST['txtCantidad']

    inv = Inventario.objects.create(codigo=codigo, articulo=articulo, cantidad=cantidad)
    messages.success(request, '¡Registro agredado!')
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

    messages.success(request, '¡Registro actualizado!')
    return redirect('/')


def eliminarArt(request, codigo):
    inv = Inventario.objects.get(codigo=codigo)
    inv.delete()

    messages.success(request, '¡Registro eliminado!')
    return redirect('/')
