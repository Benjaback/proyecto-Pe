from django.shortcuts import render, redirect, get_object_or_404
from ejemplo.models import *
from .forms import ProductoForm, ClienteForm, EmpleadoForm
from .models import Cliente, Empleado
# Create your views here.

def listar_productos(request):
    producto = Productos.objects.all()
    return render(request, "productos/listar.html", {"productos": producto})


#crear un producto
def registrar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarProductos")
    else:
        form = ProductoForm()
    return render(request, "productos/form.html", {"form": form})

#editar un producto

# def editar_producto(request,pk):
#     producto = get_object_or_404(Productos, pk=pk)
#     if request.method == "POST":
#         form = ProductoForm(request.POST, instance=producto)
#         if form.is_valid():
#             form.save()
#             return redirect('listarProductos')
#      else:
#             form = ProductoForm(instance=producto)
#     return render(request, 'productos/editar.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Productos, pk=pk)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarProductos')
    else:
        form = ProductoForm(instance=producto)  # ← Esto asegura que form se define también para GET

    return render(request, 'productos/editar.html', {'form': form})
    
#eliminar un producto

def eliminar_producto(request, pk):
    producto=get_object_or_404(Productos, pk=pk)
    producto.delete()
    return redirect('listarProductos')

#clientes

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarClientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/form.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarClientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/form.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listarClientes')
    return render(request, 'clientes/eliminar.html', {'cliente': cliente})

#Empleado
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/listar.html', {'empleados': empleados})

def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarEmpleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/form.html', {'form': form})

def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listarEmpleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/form.html', {'form': form})

def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listarEmpleados')
    return render(request, 'empleados/eliminar.html', {'empleado': empleado})
