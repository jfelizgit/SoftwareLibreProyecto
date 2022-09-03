from django.shortcuts import render, redirect
from .models import Inventario
from django.contrib import messages


# Create your views here.


def home(request):
    inventarioV = Inventario.objects.all()
    #    messages.success(request, 'Registro listado')
    return render(request, 'gestionInv.html', {'inventario': inventarioV})


def registrarArt(request):
    if request.POST:
        reg = Inventario()
        reg.codigo = request.POST.get('txtCodigo')
        reg.articulo = request.POST.get('txtArticulo')
        reg.cantidad = request.POST.get('txtCantidad')
        reg.ubicacion = request.POST.get('txtUbicacion')
        reg.imagen = request.FILES.get('image')
        reg.save()
        messages.success(request, '¡Registro agredado!')
        return redirect('/')
    return redirect('/')


def editarArt(request, codigo):
    inv = Inventario.objects.get(codigo=codigo)
    return render(request, 'editar.html', {'i': inv})


def editarInv(request):
    codigo = request.POST['txtCodigo']
    articulo = request.POST['txtArticulo']
    cantidad = request.POST['numCantidad']
    ubicacion = request.POST['txtUbicacion']
    imagen = request.FILES.get('image')

    inv = Inventario.objects.get(codigo=codigo)
    inv.articulo = articulo
    inv.cantidad = cantidad
    inv.ubicacion = ubicacion
    inv.imagen = imagen
    inv.save()

    messages.success(request, '¡Registro actualizado!')
    return redirect('/')


def eliminarArt(request, codigo):
    inv = Inventario.objects.get(codigo=codigo)
    inv.delete()

    messages.success(request, '¡Registro eliminado!')
    return redirect('/')



# registro antes de insertar imagenes
# def registrarArt(request):
#     codigo = request.POST['txtCodigo']
#     articulo = request.POST['txtArticulo']
#     cantidad = request.POST['txtCantidad']
#     ubicacion = request.POST['txtUbicacion']
#
#     if len(request.FILES) != 0:
#         Inventario.imagen = request.FILES['image']
#         Inventario.save(self=True)
#         return redirect('/')
#     inv = Inventario.objects.create(codigo=codigo, articulo=articulo, cantidad=cantidad, ubicacion=ubicacion)
#     messages.success(request, '¡Registro agredado!')
#     return redirect('/')