from django import forms
from .models import Cliente, Proyecto, Documento, Actividad

# Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["rut", "nombre", "correo", "telefono"]
        widgets = {
            "rut": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "correo": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
        }


# ----- Proyecto -----


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            "nombre_proyecto",
            "encargado_proyecto_pw",
            "encargado_proyecto_cl",
            "fk_id_cliente",
        ]
        widgets = {
            "nombre_proyecto": forms.TextInput(attrs={"class": "form-control"}),
            "encargado_proyecto_pw": forms.TextInput(attrs={"class": "form-control"}),
            "encargado_proyecto_cl": forms.TextInput(attrs={"class": "form-control"}),
            "fk_id_cliente": forms.Select(attrs={"class": "form-select"}),
        }


# ----- Documento -----


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            "codigo",
            "revision",
            "fecha_inicio",
            "fecha_fin",
            "link_drive",
            "fk_id_proyecto",
        ]
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "revision": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_inicio": forms.TextInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "fecha_fin": forms.TextInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "link_drive": forms.TextInput(attrs={"class": "form-control"}),
            "fk_id_proyecto": forms.Select(attrs={"class": "form-select"}),
        }


# ----- Actividad -----


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ["nombre_actividad", "descripcion", "fk_id_codigo"]
        widgets = {
            "nombre_documento": forms.TextInput(attrs={"class": "form-control"}),
            "revision": forms.TextInput(attrs={"class": "form-control"}),
            "fk_id_codigo": forms.Select(attrs={"class": "form-select"}),
        }
