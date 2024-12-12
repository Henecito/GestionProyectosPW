from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from usuarioApp.models import Area, Cliente, SubArea, Empleado


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["nombre", "descripcion"]
        widgets = {"nombre": forms.TextInput(attrs={"class": "form-control"}),
                   "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 2})}


class SubAreaForm(forms.ModelForm):
    class Meta:
        model = SubArea
        fields = ["nombre", "area"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "area": forms.Select(attrs={"class": "form-select"}),
        }

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
    )

    contacto_emergencia = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"placeholder": "Ej: 912345678", "class": "form-control"}
        ),
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
            "subarea",
        ]

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellidos": forms.TextInput(attrs={"class": "form-control"}),
            "nacionalidad": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "afp": forms.TextInput(attrs={"class": "form-control"}),
            "plan_salud": forms.TextInput(attrs={"class": "form-control"}),
            "carrera": forms.TextInput(attrs={"class": "form-control"}),
            "subarea": forms.Select(attrs={"class": "form-selectl"})
        }

    # Sobrescribir el método save para crear el Usuario
    def save(self, commit=True):
        # Crear el Empleado sin guardarlo todavía
        empleado = super().save(commit=False)

        # Verificar si ya existe un Usuario con el email, si no lo crea
        if not User.objects.filter(email=empleado.email).exists():
            usuario = User.objects.create_user(
                username=empleado.rut,  # Usamos el email como username
                email=empleado.email,
                password="defaultpassword",  # Cambiar esta contraseña o hacerla dinámica
                first_name=empleado.nombre,
                last_name=empleado.apellidos
            )
            # Asignamos el Usuario al Empleado
            empleado.user = usuario
        else:
            raise ValidationError("Ya existe un usuario con este correo electrónico")

        # Guardamos el Empleado, ya con el Usuario asignado
        if commit:
            empleado.save()
        return empleado


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




#Password
class PasswordChangeFormCustom(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password']
    
#Grupo
class AsignarUsuariosAGrupoForm(forms.Form):
    # Usamos ModelMultipleChoiceField para permitir seleccionar varios usuarios
    usuarios = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple(),  # Usar el widget predeterminado
        label="Selecciona usuarios",
        required=True,
    )

    # Usamos ModelChoiceField para permitir seleccionar un único grupo
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(),  # Usar el widget predeterminado
        label="Selecciona grupo",
        required=True,
    )




