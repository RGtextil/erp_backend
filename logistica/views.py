from rest_framework import generics
from .models import Producto, Proveedor
from .serializers import ProductoSerializer, ProveedorSerializer
from rest_framework.permissions import IsAuthenticated

class Productos(generics.ListCreateAPIView):
    queryset = Producto
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class ProductosDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class Proveedores(generics.ListCreateAPIView):
    queryset = Proveedor
    serializer_class = ProveedorSerializer 
    permission_classes = [IsAuthenticated]

class ProveedoresDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor
    serializer_class = ProveedorSerializer 
    permission_classes = [IsAuthenticated]
