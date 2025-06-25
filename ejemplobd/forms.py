from django import forms
from ejemplo.models import *
from .models import Cliente, Empleado
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'telefono']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'correo', 'puesto', 'telefono']