from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Precios, Volumen


class AccountCreationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=(('staff', 'Staff'), ('admin', 'Admin')),
        label='Rol',
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_superuser = self.cleaned_data['role'] == 'admin'
        if commit:
            user.save()
        return user


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