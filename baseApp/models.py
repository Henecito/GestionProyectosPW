from django.db import models
from django.contrib.auth.models import Group, Permission


# Estados
class Estado(models.Model):
    MODELOS_CHOICES = [
        ("Proyecto", "Proyecto"),
        ("Documento", "Documento"),
        ("Actividad", "Actividad"),
    ]

    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=20, choices=MODELOS_CHOICES)
    descripcion = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_modelo_display()})"

    class Meta:
        db_table = "estado"
        unique_together = ["nombre", "modelo"]
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    @classmethod
    def get_estados_por_modelo(cls, modelo):
        """
        Devuelve todos los estados para un modelo específico

        Ejemplo de uso: En una vista usar esto
        estados_proyecto = Estado.get_estados_por_modelo('Proyecto')
        """
        return cls.objects.filter(modelo=modelo)


# Grupos
# Modelo de grupo personalizado
class CustomGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    base_group = models.OneToOneField(
        Group, on_delete=models.CASCADE, related_name="custom_group"
    )
    owner = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="created_groups"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class GroupPermission(models.Model):
    custom_group = models.ForeignKey(
        CustomGroup, on_delete=models.CASCADE, related_name="permissions"
    )
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
