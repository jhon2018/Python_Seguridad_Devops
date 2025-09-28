from django.contrib import admin
from .models import Producto,Detalle

admin.site.register([Producto,Detalle]) #registrar modelos en el admin
