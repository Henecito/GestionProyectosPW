from django import forms
from django.core.validators import RegexValidator
from .models import Area, SubArea, Empleado, Asignar


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["nombre"]
        widgets = {"nombre": forms.TextInput(attrs={"class": "form-control"})}


class SubAreaForm(forms.ModelForm):
    class Meta:
        model = SubArea
        fields = ["nombre", "fk_id_area"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "fk_id_area": forms.Select(attrs={"class": "form-select"}),
        }


class EmpleadoForm(forms.ModelForm):
    # Validador de RUT chileno
    rut_validator = RegexValidator(
        regex=r"^\d{7,8}[-][0-9kK]$",
        message="Ingrese un RUT válido (formato: xxxxxxxx-x)",
    )

    # Campo de RUT con validación especial
    rut = forms.CharField(
        validators=[rut_validator],
        widget=forms.TextInput(
            attrs={"placeholder": "xxxxxxxx-x", "class": "form-control"}
        ),
    )

    # Widget personalizado para fecha de nacimiento
    fecha_nac = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )

    # Widget para teléfono con validación
    telefono = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"placeholder": "Ej: 912345678", "class": "form-control"}
        ),
        min_value=900000000,
        max_value=999999999,
    )

    # Widget para email con validación
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "ejemplo@dominio.com", "class": "form-control"}
        )
    )

    class Meta:
        model = Empleado
        fields = [
            "rut",
            "nombre",
            "apellidos",
            "email",
            "fecha_nac",
            "nacionalidad",
            "direccion",
            "afp",
            "plan_salud",
            "carrera",
            "telefono",
            "contacto_emergencia",
        ]

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellidos": forms.TextInput(attrs={"class": "form-control"}),
            "nacionalidad": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "afp": forms.TextInput(attrs={"class": "form-control"}),
            "plan_salud": forms.TextInput(attrs={"class": "form-control"}),
            "carrera": forms.TextInput(attrs={"class": "form-control"}),
            "contacto_emergencia": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_rut(self):
        # Método de validación y formateo de RUT
        rut = self.cleaned_data["rut"]

        # Eliminar posibles puntos si los hubiera
        rut = rut.replace(".", "")

        # Validación adicional del dígito verificador
        rut = rut.upper()

        # Separar cuerpo y dígito verificador
        try:
            cuerpo, dv = rut.split("-")
        except ValueError:
            raise forms.ValidationError("Formato de RUT inválido")

        # Validar que el cuerpo sean solo números
        if not cuerpo.isdigit():
            raise forms.ValidationError(
                "El RUT debe contener solo números antes del guión"
            )

        # Algoritmo de validación de RUT chileno
        def calcular_dv(rut):
            reversed_digits = map(int, reversed(str(rut)))
            factors = (2, 3, 4, 5, 6, 7)
            s = sum(d * f for d, f in zip(reversed_digits, factors * 10))
            res = (-s) % 11
            return {10: "K", 11: "0"}.get(res, str(res))

        # Verificar que el dígito verificador sea correcto
        dv_calculado = calcular_dv(int(cuerpo))
        if dv != dv_calculado:
            raise forms.ValidationError("RUT inválido")

        # Retornar el RUT formateado
        return f"{cuerpo}-{dv}"

    def clean_email(self):

        # Validación para asegurar que el email no exista previamente

        email = self.cleaned_data["email"]
        # Verificar si el email ya existe en empleados existentes
        if Empleado.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email


class AsignarForm(forms.ModelForm):
    class Meta:
        model = Asignar
        fields = ["fk_rut_empleado", "fk_id_actividad"]
        widgets = {
            "fk_rut_empleado": forms.Select(attrs={"class": "form-select"}),
            "fk_id_actividad": forms.Select(attrs={"class": "form-select"}),
        }
