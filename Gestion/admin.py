from django.contrib import admin

from Gestion.models import *

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "tel")
    search_fields=("nombre", "tel")

admin.site.register(Clientes, ClientesAdmin)


class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre", "seccion", "precio")
    list_filter=("seccion",)

admin.site.register(Articulos, ArticulosAdmin)


class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",) 
    date_hierarchy="fecha"

admin.site.register(Pedidos, PedidosAdmin)
