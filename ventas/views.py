from rest_framework import generics, permissions
from .serializers import ClienteSerializer, PedidoSerializer
from .models import Clientes, PedidoCliente

class ClientesView(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Clientes.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class ClienteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Solo mostrar las casas del usuario logueado
        return Clientes.objects.filter(usuario=self.request.user)


class PedidoClientesView(generics.ListCreateAPIView):
    queryset = PedidoCliente.objects.all()
    serializer_class = PedidoSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo mostrar las casas del usuario logueado
        return PedidoCliente.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class PedidoClienteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PedidoCliente.objects.all()
    serializer_class =  PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo mostrar las casas del usuario logueado
        return PedidoCliente.objects.filter(usuario=self.request.user)


    