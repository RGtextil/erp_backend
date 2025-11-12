from django.urls import path
from .views import Productos, ProductoDetails,ProveedorDetails, Proveedores

urlpatterns = [
    path('producto/',Productos.as_view(), name='producto'),
    path('producto/<int:pk>/',ProductoDetails.as_view(), name='productodetail'),
    path('proveedor/',Proveedores.as_view(),name='proveedor'),
    path('proveedor/<int:pk>/',ProveedorDetails.as_view(),name='proveedordatail'),
]

