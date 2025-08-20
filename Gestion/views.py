from django.shortcuts import render
from django.http import HttpResponse
from Gestion.models import *

# Create your views here.

def buscar_productos(request):
    return render(request, "buscar_productos.html")


def buscar(request):
    
    if request.GET["pro"]:
        #mensaje = "Artículo buscado: %r" %request.GET["pro"]
        prod = request.GET["pro"]
        art = Articulos.objects.filter(nombre__icontains=prod)
        return render(request, "resultados_busqueda.html", {"articulos": art, "query": prod})


    else:
        mensaje = "No has introducido ningún valor, por favor vuelve a intentarlo."

    return HttpResponse(mensaje)
