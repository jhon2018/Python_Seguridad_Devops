# webproductos/apis/views.py
# OBJETIVO: crear las vistas de la app apis para mostrar los productos en formato JSON
from rest_framework import viewsets
from .serealizers import ArticuloSerializer
from .models import Articulos

"""
METODOS HTTP
GET: obtener datos
POST: crear datos
PUT: actualizar datos
DELETE: eliminar datos
PATCH: actualizar parcialmente datos
"""

#crear una vista basada en clases (viewsets) que hereda de ModelViewSet y permite realizar operaciones CRUD
class ArticuloViewSet(viewsets.ModelViewSet): 
    queryset = Articulos.objects.all() #traer todos los objetos de la clase Articulos
    serializer_class = ArticuloSerializer 



