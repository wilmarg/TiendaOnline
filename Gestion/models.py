from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(max_length=7)

    def __str__(self):
        return 'Cliente: "%s" -- Tel: "%s"' %(self.nombre, self.tel)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'Artículo: "%s" -- Sección: "%s" -- Precio: $%s' %(self.nombre, self.seccion, self.precio)
    


class Pedidos(models.Model):
    precio = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()




