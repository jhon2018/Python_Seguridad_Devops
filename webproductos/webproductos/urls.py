from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/', include('apis.urls')),

]



"""
RUTAS DE LA API
GET: http://127.0.0.1:8000/api/articulos/
POST: http://127.0.0.1:8000/api/articulos/
PUT: http://127.0.0.1:8000/api/articulos/1/
DELETE: http://127.0.0.1:8000/api/articulos/1/
"""