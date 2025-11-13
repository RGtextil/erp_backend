from django.urls import path
from .views import ClientesView,ClienteDetails,PedidoClientesView,PedidoClienteDetails

urlpatterns = [
    path('cliente/',ClientesView.as_view(), name='cliente'),
    path('cliente/<int:pk>/',ClienteDetails.as_view(), name='clientedetail'),
    path('pedido/',PedidoClientesView.as_view(),name='pedido'),
    path('pedido/<int:pk>/',PedidoClienteDetails.as_view(),name='pedidodetail'),
]


