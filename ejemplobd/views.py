from django.shortcuts import render, redirect, get_object_or_404
from ejemplo.models import *
from .forms import ProductoForm
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