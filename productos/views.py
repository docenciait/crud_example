from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto


# Create your views here.

productos = []

def index(request):
    return render(request, 'index.html')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos' : productos})

def agregar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        cantidad = request.POST.get("cantidad")
        Producto.objects.create(nombre=nombre, precio=precio, cantidad=cantidad) 
        return redirect('productos:listar_productos')
    return render(request, "agregar.html")

def eliminar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        try:
            producto = Producto.objects.get(nombre=nombre)
            producto.delete()
        except Producto.DoesNotExist:
            pass
        
        return redirect('productos:listar_productos')

    return render(request, "eliminar.html")  