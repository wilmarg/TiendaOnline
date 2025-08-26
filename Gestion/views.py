from django.shortcuts import render
from django.http import HttpResponse
from Gestion.models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def buscar_productos(request):
    return render(request, "buscar_productos.html")


def buscar(request):
    
    if request.GET["pro"]:
        #mensaje = "Artículo buscado: %r" %request.GET["pro"]
        prod = request.GET["pro"]
        
        if len(prod)>20:

            mensaje = "Texto introducido demasiado largo, intente de nuevo..."
        
        else:

            art = Articulos.objects.filter(nombre__icontains=prod)
            return render(request, "resultados_busqueda.html", {"articulos": art, "query": prod})


    else:
        mensaje = "No has introducido ningún valor, por favor vuelve a intentarlo."

    return HttpResponse(mensaje)



def contacto(request):

    if request.method == "POST":

        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["wilmar.galvis.294@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, "gracias.html")

    return render(request, "contacto.html")



