from django.db import models
from django.core.validators import URLValidator, RegexValidator
from baseApp.models import Estado


class Cliente(models.Model):
    rut_validator = RegexValidator(
        regex=r"^\d{7,8}[-][0-9kK]$",
        message="Ingrese un RUT válido (formato: xxxxxxxx-x)",
    )

    telefono_validator = RegexValidator(
        regex=r"^(\+?56)?(\s?)(0?9)(\s?)[9876543]\d{7}$",
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


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    encargado_proyecto_pw = models.CharField(max_length=50)
    encargado_proyecto_cl = models.CharField(max_length=50)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    fk_id_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="proyectos"
    )
    fk_id_estado = models.ForeignKey(
        Estado, null=True, on_delete=models.CASCADE, related_name="proyectos"
    )

    def __str__(self):
        return self.nombre_proyecto

    class Meta:
        db_table = "proyecto"
        verbose_name_plural = "Proyectos"


class Documento(models.Model):
    codigo = models.CharField(max_length=50, primary_key=True)
    revision = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    link_drive = models.URLField(
        max_length=200, validators=[URLValidator()], null=True, blank=True
    )
    fk_id_proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, related_name="documentos"
    )
    fk_id_estado = models.ForeignKey(
        Estado, on_delete=models.CASCADE, related_name="documentos"
    )

    def __str__(self):
        return self.revision

    class Meta:
        db_table = "documento"
        verbose_name_plural = "Documentos"


class Actividad(models.Model):
    nombre_actividad = models.CharField(max_length=50)
    descripcion = models.TextField()  # Cambié a TextField para descripción más larga
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    duracion_estimada = models.DurationField(null=True, blank=True)
    fk_id_codigo = models.ForeignKey(
        Documento, on_delete=models.CASCADE, related_name="actividades"
    )
    fk_id_estado = models.ForeignKey(
        Estado, on_delete=models.CASCADE, related_name="actividades"
    )

    def __str__(self):
        return self.nombre_actividad

    class Meta:
        db_table = "actividad"
        verbose_name_plural = "Actividades"
