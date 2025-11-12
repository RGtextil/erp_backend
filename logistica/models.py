from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User 
from django.conf import settings

class Producto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
    producto_nombre = models.CharField(max_length=20)
    producto_color = models.CharField(max_length=20)
    producto_metros = models.IntegerField()

    def __str__(self):
        return self.producto_nombre
    
class Proveedor(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()

    def __srt__(self):
        return self.nombre
    
=======

class Producto(models.Model):
        producto_nombre = models.CharField(max_length=20)
        producto_color = models.CharField(max_length=20)
        producto_metros = models.IntegerField()
        producto_creacion = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.producto_nombre

class Proveedor(models.Model):
        proveedor_nombre = models.CharField(max_length=20)
        proveedor_ciudad = models.CharField(max_length=20)
        proveedor_telefono = models.IntegerField()

        def __str__(self):
            return self.proveedor_nombre

>>>>>>> 0c1658b9099aa6ae43392d0bf5877bd3687095e0
