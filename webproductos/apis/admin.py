# webproductos/apis/admin.py
# Objetivo: registrar los modelos en el admin

from django.contrib import admin
from .models import Articulos

admin.site.register(Articulos) #registrar modelos en el admin
