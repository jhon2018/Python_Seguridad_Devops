# webproductos/core/urls.py
# En este archivo se definen las rutas para las vistas de la aplicación core.
from django.urls import path
from .views import lista_productos,detalle_producto

urlpatterns = [
    path('', lista_productos),
    path('detalles/', detalle_producto), 
]