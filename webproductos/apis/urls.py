# webproductos/apis/urls.py
# OBJETIVO: definir las rutas de la app apis y conectarlas con las vistas

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet

router = DefaultRouter()
router.register('articulos', ArticuloViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
 
