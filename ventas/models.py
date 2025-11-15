from django.db import models
from django.conf import settings

class Clientes(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="clientes")
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class PedidoCliente(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pedidosclientes")
    cliente = models.CharField(max_length=20)
    tela = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __srt__(self):
        return self.cliente
    