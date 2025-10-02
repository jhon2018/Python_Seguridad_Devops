# webproductos/core/views.py
# se realizan las vistas y se llaman desde las urls para ser mostradas en el navegador y poder interactuar con la base de datos.
from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render (request, "index.html", {"productos": productos}) #devuelve el archivo index.html y le pasa el diccionario de productos

def detalle_producto(request):
    return render(request, "detalles.html")  # devuelve el archivo detalle_producto.html


