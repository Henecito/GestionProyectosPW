# Generated by Django 5.1.3 on 2024-11-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Apellido')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está activo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Es staff')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Último inicio de sesión')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
