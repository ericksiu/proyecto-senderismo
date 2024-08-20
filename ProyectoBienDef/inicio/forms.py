# inicio/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from modelos.models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('imagen','email', 'nombre', 'apellidos', 'telefono', 'ciudad', 'estado', 'tarjeta', 'cvv', 'caducidad')

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nombre', 'apellidos', 'telefono', 'email', 'ciudad', 'estado', 'imagen', 'tarjeta', 'cvv', 'caducidad']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nombre', 'apellidos', 'telefono', 'email', 'ciudad', 'estado', 'imagen', 'tarjeta', 'cvv', 'caducidad']




