from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from webLimpieza.models import Actividad, Cuadrilla, Empleado, Colonia

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['cuadri', 'foto', 'id_colonia', 'detalle']
        labels = {
            'cuadri': 'Nombre de Cuadrilla',
            'foto': 'Foto',
            'id_colonia': 'ID Colonia',
            'detalle': 'Detalle',
        }
        widgets = {
            'cuadri' : forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'frmFoto'}),
            'id_colonia': forms.Select(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'frmDetalle'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'paterno', 'materno', 'telefono', 'puesto', 'cuadri']
        labels = {
            'nombre': 'Nombre',
            'paterno': 'Apellido Paterno',
            'materno': 'Apellido Materno',
            'telefono': 'Telefono',
            'puesto': 'Puesto',
            'cuadri': 'Cuadrilla',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'materno': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.Select(choices=[
                ('Trabajador', 'Trabajador'),
                ('Gerente', 'Gerente'),
                ('Jefe de Cuadrilla', 'Jefe de Cuadrilla'),
            ], attrs={'class': 'form-control'}),
            'cuadri': forms.Select(attrs={'class': 'form-control'}),
        }

class CuadrillaForm(forms.ModelForm):
    class Meta:
        model = Cuadrilla
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre de la cuadrilla',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ColoniaForm(forms.ModelForm):
    class Meta:
        model = Colonia
        fields = ['nombre', 'cod_postal']
        labels = {
            'nombre': 'Nombre',
            'cod_postal': 'Codigo Postal',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre de la cuadrilla',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_postal': forms.TextInput(attrs={'class': 'form-control'}),
        }