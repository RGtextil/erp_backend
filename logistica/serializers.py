from rest_framework import serializers
<<<<<<< HEAD
from .models import Producto, Proveedor

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


=======
from .models import Producto, Proveedor 

class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

        
>>>>>>> 0c1658b9099aa6ae43392d0bf5877bd3687095e0
