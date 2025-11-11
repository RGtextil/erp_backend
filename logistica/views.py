from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductoSerializer, ProveedorSerializer
from .models import Producto, Proveedor

class Productos(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class Proveedores(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class =  ProveedorSerializer

class ProveedorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class =  ProveedorSerializer

    