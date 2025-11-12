<<<<<<< HEAD
from django.urls import path
from .views import Productos, ProductoDetails,ProveedorDetails, Proveedores

urlpatterns = [
    path('producto/',Productos.as_view(), name='producto'),
    path('producto/<int:pk>/',ProductoDetails.as_view(), name='productodetail'),
    path('proveedor/',Proveedores.as_view(),name='proveedor'),
    path('proveedor/<int:pk>/',ProveedorDetails.as_view(),name='proveedordatail'),
]

=======
from django.urls import path 
from . import views 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('producto/',views.Productos.as_view()),
    path('producto/<int:pk>',views.ProductosDetails.as_view()),
    path('proveedores/',views.Proveedores.as_view()),
    path('proveedores/<int:pk>',views.ProveedoresDetails.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
>>>>>>> 0c1658b9099aa6ae43392d0bf5877bd3687095e0
