<<<<<<< HEAD
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ProductoSerializer, ProveedorSerializer
from .models import Producto, Proveedor
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin

class Productos(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Solo mostrar las casas del usuario logueado
        return Producto.objects.filter(usuario=self.request.user)

class ProductoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        # Solo mostrar las casas del usuario logueado
        return Producto.objects.filter(usuario=self.request.user)


class Proveedores(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class =  ProveedorSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Solo mostrar las casas del usuario logueado
        return Proveedor.objects.filter(usuario=self.request.user)


class ProveedorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class =  ProveedorSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Solo mostrar las casas del usuario logueado
        return Proveedor.objects.filter(usuario=self.request.user)


    
=======
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
>>>>>>> 0c1658b9099aa6ae43392d0bf5877bd3687095e0
