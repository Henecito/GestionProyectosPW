from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, RegexValidator
from baseApp.models import Estado
from usuarioApp.models import Cliente, Empleado


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    cliente = models.ForeignKey(
        Cliente,
        null=True,
        on_delete=models.SET_NULL,
        related_name="proyectos",
        verbose_name="Cliente",
    )
    encargado = models.ForeignKey(
        Empleado,
        null=True,
        on_delete=models.SET_NULL,
        related_name="proyectos",
        verbose_name="Encargado",
    )
    # encargado_proyecto_cl = models.CharField(max_length=50)
    fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha Inicio")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha Fin")
    estado = models.ForeignKey(
        Estado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"modelo": "Proyecto"},
        related_name="proyectos",
        verbose_name="Estado",
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
        return self.fecha_inicio.strftime("%d/%m/%Y") if self.fecha_inicio else ""

    def get_fecha_fin_formatted(self):
        return self.fecha_fin.strftime("%d/%m/%Y") if self.fecha_fin else ""


class Documento(models.Model):
    codigo = models.CharField(max_length=50, primary_key=True, verbose_name="Código")
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name="documentos",
        verbose_name="Proyecto",
    )
    # revision = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha Inicio")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha Fin")
    link_drive = models.URLField(
        max_length=200,
        validators=[URLValidator()],
        null=True,
        blank=True,
        verbose_name="Link Drive",
    )
    estado = models.ForeignKey(
        Estado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"modelo": "Documento"},
        related_name="documentos",
        verbose_name="Estado",
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
        return self.fecha_inicio.strftime("%d/%m/%Y") if self.fecha_inicio else ""

    def get_fecha_fin_formatted(self):
        return self.fecha_fin.strftime("%d/%m/%Y") if self.fecha_fin else ""


class Actividad(models.Model):
    # nombre = models.CharField(max_length=50)
    documento = models.ForeignKey(
        Documento,
        on_delete=models.CASCADE,
        related_name="actividades",
        verbose_name="Documento",
    )
    descripcion = models.TextField(max_length=200, verbose_name="Descripción")
    encargado = models.ForeignKey(
        Empleado,
        null=True,
        on_delete=models.SET_NULL,
        related_name="actividades",
        verbose_name="Encargado",
    )
    fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha Inicio")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha Fin")
    # duracion_estimada = models.DurationField(null=True, blank=True)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"modelo": "Actividad"},
        related_name="actividades",
        verbose_name="Estado",
    )
    comentario = models.TextField(blank=True, null=True, verbose_name="Comentario")

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
        return self.fecha_inicio.strftime("%d/%m/%Y") if self.fecha_inicio else ""

    def get_fecha_fin_formatted(self):
        return self.fecha_fin.strftime("%d/%m/%Y") if self.fecha_fin else ""


class Asignar(models.Model):
    empleado = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, related_name="asignaciones"
    )
    actividad = models.ForeignKey(
        Actividad, on_delete=models.CASCADE, related_name="asignaciones"
    )
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["empleado", "actividad"]
        verbose_name_plural = "Asignaciones"

    def __str__(self):
        return f"{self.empleado} - {self.actividad}"
