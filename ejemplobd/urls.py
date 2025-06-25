from django.urls import path
from ejemplobd.views import *
from . import views

urlpatterns = [
    path('productos/', listar_productos, name='listarProductos'),
    path('productos/registrar/', registrar_producto, name='registrarProducto'),
    path('editar/<int:pk>/', editar_producto, name='editarProducto'),
    path('eliminar/<int:pk>/', eliminar_producto, name='eliminarProducto'),
    #clientes
    path('clientes/', views.listar_clientes, name='listarClientes'),
    path('clientes/registrar/', views.registrar_cliente, name='registrarCliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editarCliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminarCliente'),
    #empleados
    path('empleados/', views.listar_empleados, name='listarEmpleados'),
    path('empleados/registrar/', views.registrar_empleado, name='registrarEmpleado'),
    path('empleados/editar/<int:pk>/', views.editar_empleado, name='editarEmpleado'),
    path('empleados/eliminar/<int:pk>/', views.eliminar_empleado, name='eliminarEmpleado'),
]

