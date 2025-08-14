from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(max_length=7)

    ##ef __str__(self):
    ##    return 'Cliente: "%s" ' %(self.nombre)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20, verbose_name="Sección")
    precio = models.IntegerField()

    #def __str__(self):
    #    return 'Artículo: "%s" -- Sección: "%s" -- Precio: $%s' %(self.nombre, self.seccion, self.precio)
    


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()




