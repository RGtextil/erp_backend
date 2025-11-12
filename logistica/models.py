from django.db import models

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

