from django.urls import path
from ejemplobd.views import *
from . import views

urlpatterns = [
    path('productos/', listar_productos, name='listarProductos'),
    path('productos/registrar/', registrar_producto, name='registrarProducto'),
    path('editar/<int:pk>/', editar_producto, name='editarProducto'),
    path('eliminar/<int:pk>/', eliminar_producto, name='eliminarProducto'),
    path('clientes/', views.listar_clientes, name='listarClientes'),
    path('clientes/registrar/', views.registrar_cliente, name='registrarCliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editarCliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminarCliente'),
]

