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