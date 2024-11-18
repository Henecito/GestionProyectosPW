from django.db import models

# Create your models here.

class Proyecto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=60)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    # estado = models.ForeignKey(Cargo, null=False, on_delete=models.RESTRICT)
    lider = models.CharField(max_length=100)
    presupuesto = models.FloatField()
    observaciones = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'proyecto'