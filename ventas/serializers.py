from rest_framework import serializers
from .models import Clientes, PedidoCliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Clientes
        fields = '__all__'
        read_only_fields = ['usuario'] 
        
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCliente
        fields = '__all__'
        read_only_fields = ['usuario'] 
        
