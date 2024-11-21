from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

# Definición del Manager antes de la clase Usuario
class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico.")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)

# Luego se define la clase Usuario
class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, verbose_name="Nombre de usuario")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    first_name = models.CharField(max_length=150, blank=True, verbose_name="Nombre")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="Apellido")
    is_active = models.BooleanField(default=True, verbose_name="Está activo")
    is_staff = models.BooleanField(default=False, verbose_name="Es staff")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    last_login = models.DateTimeField(null=True, blank=True, verbose_name="Último inicio de sesión")

    # Usamos el manager aquí
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'  # Campo usado para autenticación
    REQUIRED_FIELDS = ['username']  # Campos requeridos además de USERNAME_FIELD

    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',  # Cambio de related_name aquí
        blank=True,
        verbose_name="Grupos"
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_set',  # Cambio de related_name aquí
        blank=True,
        verbose_name="Permisos"
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username

