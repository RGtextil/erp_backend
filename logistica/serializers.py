from rest_framework import serializers
from .models import Producto, Proveedor, PedidoProveedor 

class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields = '__all__'
        read_only_fields = ['usuario'] 
        
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        read_only_fields = ['usuario'] 
        
class PedidoProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoProveedor
        fields = '__all__'
        read_only_fields = ['usuario'] 

