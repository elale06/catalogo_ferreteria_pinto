from django import forms

from .models import Precios, Volumen


class VolumenForm(forms.ModelForm):
    class Meta:
        model = Volumen
        fields = ('id', 'nombre', 'categoria', 'stock')
        labels = {
            'id': 'Código',
            'nombre': 'Nombre',
            'categoria': 'Categoría',
            'stock': 'Stock',
        }


class PreciosForm(forms.ModelForm):
    precio = forms.DecimalField(
        required=False,
        min_value=0,
        decimal_places=0,
        max_digits=10,
        label='Precio unitario',
        widget=forms.NumberInput(attrs={'min': '0', 'step': '1', 'placeholder': 'Ej. 12990'}),
    )

    class Meta:
        model = Precios
        fields = ('precio', 'moneda', 'observacion')
        labels = {
            'precio': 'Precio unitario',
            'moneda': 'Moneda',
            'observacion': 'Observación',
        }
        widgets = {
            'moneda': forms.TextInput(attrs={'placeholder': 'CLP'}),
            'observacion': forms.TextInput(attrs={'placeholder': 'Opcional'}),
        }