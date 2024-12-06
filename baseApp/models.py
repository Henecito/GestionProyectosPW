from django.db import models


class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    desc = models.TextField(max_length=300)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "estado"
        verbose_name_plural = "Estados"
