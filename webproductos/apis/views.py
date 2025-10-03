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

#crear una vista basada en clases (viewsets) que hereda de ModelViewSet y permite realizar operaciones CRUD de forma automática a través de la API
class ArticuloViewSet(viewsets.ModelViewSet): 
    queryset = Articulos.objects.all() #traer todos los objetos de la clase Articulos
    serializer_class = ArticuloSerializer 





"""
UTILIZANDO APIVIEW Y RESPONSE
"""
from rest_framework.views import APIView
from rest_framework.response import Response #importar Response para devolver respuestas HTTP
from rest_framework import status #importar status para devolver códigos de estado HTTP

class ArticulosListCreateAPIView(APIView):
    def get(self, request): #método GET para obtener todos los artículos
        articulos = Articulos.objects.all()
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data)

    def post(self, request): #método POST para crear un nuevo artículo
        serializer = ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)