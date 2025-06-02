from django import forms
from ejemplo.models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"
