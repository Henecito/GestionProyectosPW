from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, RegexValidator
from baseApp.models import Estado


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


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    encargado = models.CharField(max_length=50)
    # encargado_proyecto_cl = models.CharField(max_length=50)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="proyectos"
    )
    estado = models.ForeignKey(
        Estado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"modelo": "Proyecto"},
        related_name="proyectos",
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "proyecto"
        verbose_name_plural = "Proyectos"

    def clean(self):
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_inicio > self.fecha_fin:
                raise ValidationError(
                    {
                        "fecha_fin": "La fecha de fin debe ser posterior a la fecha de inicio"
                    }
                )
            
    def get_fecha_inicio_formatted(self):
        return self.fecha_inicio.strftime('%d/%m/%Y') if self.fecha_inicio else ''

    def get_fecha_fin_formatted(self):
        return self.fecha_fin.strftime('%d/%m/%Y') if self.fecha_fin else ''


class Documento(models.Model):
    codigo = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=200)
    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, related_name="documentos"
    )
    revision = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    link_drive = models.URLField(
        max_length=200, validators=[URLValidator()], null=True, blank=True
    )
    estado = models.ForeignKey(
        Estado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"modelo": "Documento"},
        related_name="documentos",
    )

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = "documento"
        verbose_name_plural = "Documentos"

    def clean(self):
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_inicio > self.fecha_fin:
                raise ValidationError(
                    {
                        "fecha_fin": "La fecha de fin debe ser posterior a la fecha de inicio"
                    }
                )
            
    def get_fecha_inicio_formatted(self):
        return self.fecha_inicio.strftime('%d/%m/%Y') if self.fecha_inicio else ''

    def get_fecha_fin_formatted(self):
        return self.fecha_fin.strftime('%d/%m/%Y') if self.fecha_fin else ''


class Actividad(models.Model):
    # nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    documento = models.ForeignKey(
        Documento, on_delete=models.CASCADE, related_name="actividades"
    )
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    duracion_estimada = models.DurationField(null=True, blank=True)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"modelo": "Actividad"},
        related_name="actividades",
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "actividad"
        verbose_name_plural = "Actividades"

    def clean(self):
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_inicio > self.fecha_fin:
                raise ValidationError(
                    {
                        "fecha_fin": "La fecha de fin debe ser posterior a la fecha de inicio"
                    }
                )
            
    def get_fecha_inicio_formatted(self):
        return self.fecha_inicio.strftime('%d/%m/%Y') if self.fecha_inicio else ''

    def get_fecha_fin_formatted(self):
        return self.fecha_fin.strftime('%d/%m/%Y') if self.fecha_fin else ''
