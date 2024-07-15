from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'img']
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
