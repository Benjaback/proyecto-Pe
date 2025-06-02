from django.urls import path
from ejemplobd.views import *

urlpatterns = [
    path('productos/', listar_productos, name='listarProductos'),
    path('productos/registrar/', registrar_producto, name='registrarProducto'),
    path('editar/<int:pk>/', editar_producto, name='editarProducto'),
    path('eliminar/<int:pk>/', eliminar_producto, name='eliminarProducto'),
]