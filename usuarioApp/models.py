from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User as Usuario
from django.core.validators import RegexValidator


class Area(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "area"
        verbose_name_plural = "Areas"


class SubArea(models.Model):
    nombre = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="subareas")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "subarea"
        verbose_name_plural = "SubAreas"


class Cliente(models.Model):
    rut_validator = RegexValidator(
        regex=r"^\d{7,8}[-][0-9kK]$",
        message="Ingrese un RUT válido (formato: xxxxxxxx-x)",
    )

    telefono_validator = RegexValidator(
        regex=r"^(\+?56)?(\s?)(0?9)(\s?)[98765432]\d{7}$",
        message="Ingrese un número de teléfono válido",
    )

    rut = models.CharField(primary_key=True, max_length=12, validators=[rut_validator])
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=12, validators=[telefono_validator])

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "cliente"
        verbose_name_plural = "Clientes"


class Empleado(models.Model):
    rut_validator = RegexValidator(
        regex=r"^\d{7,8}[-][0-9kK]$",
        message="Ingrese un RUT válido (formato: xxxxxxxx-x)",
    )

    telefono_validator = RegexValidator(
        regex=r"^(\+?56)?(\s?)(0?9)(\s?)[98765432]\d{7}$",
        message="Ingrese un número de teléfono válido",
    )

    rut = models.CharField(primary_key=True, max_length=12, validators=[rut_validator])
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    fecha_nac = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    afp = models.CharField(max_length=50)
    plan_salud = models.CharField(max_length=50)
    carrera = models.CharField(max_length=100)

    telefono = models.CharField(max_length=12, validators=[telefono_validator])
    contacto_emergencia = models.CharField(
        max_length=12, validators=[telefono_validator]
    )

    subarea = models.ForeignKey(
        SubArea, null=True, on_delete=models.SET_NULL, related_name="empleados"
    )
    user = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="empleado",
    )

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    class Meta:
        db_table = "empleado"
        verbose_name_plural = "Empleados"


# Señal para creación de usuario
@receiver(post_save, sender=Empleado)
def crear_usuario_empleado(sender, instance, created, **kwargs):
    if created and not hasattr(instance, "user"):
        try:
            usuario = Usuario.objects.create_user(
                username=instance.rut,
                email=instance.email,
                first_name=instance.nombre,
                last_name=instance.apellidos,
                password=Usuario.objects.make_random_password(),
            )

            # Asociar el usuario al empleado
            instance.user = usuario
            instance.save()
        except Exception as e:
            # Manejar cualquier error en la creación de usuario
            print(f"Error al crear usuario: {e}")
