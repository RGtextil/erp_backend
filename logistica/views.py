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


    