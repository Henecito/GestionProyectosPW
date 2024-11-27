from django.db import models


class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField()
    email = models.EmailField()
    fecha_creacion = models.DateField(auto_created=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "cliente"


class Proyecto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=60)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    # estado = models.ForeignKey(Estado, null=False, on_delete=models.RESTRICT)
    # cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    lider = models.CharField(max_length=100)
    presupuesto = models.FloatField()
    observaciones = models.TextField()
    fecha_creacion = models.DateField(auto_created=True)
    fecha_modificacion = models.DateField(auto_created=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "proyecto"
