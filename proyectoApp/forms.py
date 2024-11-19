from django import forms
from proyectoApp.models import Proyecto


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
            "fecha_creacion",
            "fecha_modificacion",
        ]  # Todos los campos "__all__"
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
            # "cliente": forms.Select(attrs={"class": "form-select"}),
            "lider": forms.TextInput(attrs={"class": "form-control"}),
            "presupuesto": forms.NumberInput(attrs={"class": "form-control"}),
            "observaciones": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_creacion": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "fecha_modificacion": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }
