from django.urls import path
from .views import Productos, ProductoDetails,ProveedorDetails, Proveedores,PedidoProveedorView, PedidoProveedorDetails

urlpatterns = [
    path('producto/',Productos.as_view(), name='producto'),
    path('producto/<int:pk>/',ProductoDetails.as_view(), name='productodetail'),
    path('proveedor/',Proveedores.as_view(),name='proveedor'),
    path('proveedor/<int:pk>/',ProveedorDetails.as_view(),name='proveedordatail'),
    path('pedido/',PedidoProveedorView.as_view(),name='proveedorpedido'),
    path('pedido/<int:pk>/',PedidoProveedorDetails.as_view(),name='proveedordatailpedido'),
]


