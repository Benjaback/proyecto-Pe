from django import forms
from ejemplo.models import *
from .models import Cliente
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'telefono']