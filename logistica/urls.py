from django.urls import path
from .views import Productos, ProductoDetails,ProveedorDetails, Proveedores

urlpatterns = [
    path('producto/',Productos.as_view()),
    path('productoDetail/<int:pk>/',ProductoDetails.as_view()),
    path('proveedor/',Proveedores.as_view()),
    path('proveedorDetail/<int:pk>/',ProveedorDetails.as_view()),
]

