from django import forms
from django.core.exceptions import ValidationError

from baseApp.models import Estado
from proyectoApp.models import Asignar, Proyecto, Documento, Actividad


# Proyecto


class ProyectoForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],  # Formatos aceptados
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'
        )
    )
    fecha_fin = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'
        ),
        required=False  # Si el campo puede estar vacío
    )
    
    class Meta:
        model = Proyecto
        fields = [
            "nombre",
            "cliente",
            "encargado",
            "fecha_inicio",
            "fecha_fin",
            "estado",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "cliente": forms.Select(attrs={"class": "form-select"}),
            "encargado": forms.Select(attrs={"class": "form-select"}),
            # "encargado_proyecto_cl": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_inicio": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "fecha_fin": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")

        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            raise forms.ValidationError(
                {"fecha_fin": "La fecha de fin debe ser posterior a la fecha de inicio"}
            )

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limitar estados solo a Proyecto
        self.fields["estado"].queryset = Estado.get_estados_por_modelo("Proyecto")


# Documento


class DocumentoForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],  # Formatos aceptados
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'
        )
    )
    fecha_fin = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'
        ),
        required=False  # Si el campo puede estar vacío
    )

    class Meta:
        model = Documento
        fields = [
            "codigo",
            "nombre",
            "proyecto",
            # "revision",
            "fecha_inicio",
            "fecha_fin",
            "link_drive",
            "estado",
        ]
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "proyecto": forms.Select(attrs={"class": "form-select"}),
            # "revision": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_inicio": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "fecha_fin": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "link_drive": forms.URLInput(attrs={"class": "form-control"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")

        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            raise forms.ValidationError(
                {"fecha_fin": "La fecha de fin debe ser posterior a la fecha de inicio"}
            )

        return cleaned_data

    def clean_link_drive(self):
        link = self.cleaned_data.get("link_drive")
        if link:
            # Validaciones adicionales
            if not link.startswith(
                ("https://drive.google.com", "http://drive.google.com")
            ):
                raise forms.ValidationError(
                    "Por favor, ingrese un enlace de Google Drive válido"
                )
        return link

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limitar estados solo a Documento
        self.fields["estado"].queryset = Estado.get_estados_por_modelo("Documento")


# Actividad


class ActividadForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],  # Formatos aceptados
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'
        )
    )
    fecha_fin = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'
        ),
        required=False  # Si el campo puede estar vacío
    )

    class Meta:
        model = Actividad
        fields = [
            # "nombre",
            "documento",
            "descripcion",
            "encargado",
            "fecha_inicio",
            "fecha_fin",
            # "duracion_estimada",
            "estado",
        ]
        widgets = {
            # "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "documento": forms.Select(attrs={"class": "form-select"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "encargado": forms.Select(attrs={"class": "form-select"}),
            "fecha_inicio": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "fecha_fin": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            # "duracion_estimada": forms.TextInput(attrs={"class": "form-control"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")

        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            raise forms.ValidationError(
                {"fecha_fin": "La fecha de fin debe ser posterior a la fecha de inicio"}
            )

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limitar estados solo a Actividad
        self.fields["estado"].queryset = Estado.get_estados_por_modelo("Actividad")

class ActividadEncargadoForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['estado', 'comentario']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configurar los campos para que sean requeridos o no
        self.fields['estado'].required = False
        self.fields['comentario'].required = False
        
        # Personalizar widgets si es necesario
        self.fields['estado'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Seleccionar Estado'
        })
        self.fields['comentario'].widget.attrs.update({
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Agregar comentario (opcional)'
        })
        
        # Limitar estados solo a Actividad
        self.fields['estado'].queryset = Estado.get_estados_por_modelo("Actividad")

class AsignarForm(forms.ModelForm):
    class Meta:
        model = Asignar
        fields = ["empleado", "actividad"]
        widgets = {
            "empleado": forms.Select(attrs={"class": "form-select"}),
            "actividad": forms.Select(attrs={"class": "form-select"}),
        }