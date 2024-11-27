from django import forms
from proyectoApp.models import Cliente, Proyecto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            "rut",
            "nombre",
            "telefono",
            "email",
        ]
        widgets = {
            "rut": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.NumberInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            "codigo",
            "nombre",
            # "descripcion",
            "fecha_inicio",
            "fecha_fin",
            "lider",
            "presupuesto",
            "observaciones",
        ]
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            # "descripcion": forms.TextInput(attrs={"class": "form-control", "rows": 2}),
            "fecha_inicio": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "fecha_fin": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            # "estado": forms.Select(attrs={"class": "form-select"}),
            "cliente": forms.Select(attrs={"class": "form-select"}),
            "lider": forms.Select(attrs={"class": "form-select"}),
            "presupuesto": forms.NumberInput(attrs={"class": "form-control"}),
            "observaciones": forms.TextInput(attrs={"class": "form-control"}),
        }
