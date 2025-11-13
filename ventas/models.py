from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class PedidoCliente(models.Model):
    cliente = models.CharField(max_length=20)
    tela = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __srt__(self):
        return self.cliente
    