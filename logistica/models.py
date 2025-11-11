from django.db import models

class Producto(models.Model):
    producto_nombre = models.CharField(max_length=20)
    producto_color = models.CharField(max_length=20)
    producto_metros = models.IntegerField()

    def __str__(self):
        return self.producto_nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()

    def __srt__(self):
        return self.nombre
    
