# Generated by Django 5.1.3 on 2024-12-12 02:45

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Areas',
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Ingrese un RUT válido (formato: xxxxxxxx-x)', regex='^\\d{7,8}[-][0-9kK]$')])),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Ingrese un número de teléfono válido', regex='^(\\+?56)?(\\s?)(0?9)(\\s?)[98765432]\\d{7}$')])),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='SubArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subareas', to='usuarioApp.area')),
            ],
            options={
                'verbose_name_plural': 'SubAreas',
                'db_table': 'subarea',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Ingrese un RUT válido (formato: xxxxxxxx-x)', regex='^\\d{7,8}[-][0-9kK]$')])),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fecha_nac', models.DateField()),
                ('nacionalidad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('afp', models.CharField(max_length=50)),
                ('plan_salud', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Ingrese un número de teléfono válido', regex='^(\\+?56)?(\\s?)(0?9)(\\s?)[98765432]\\d{7}$')])),
                ('contacto_emergencia', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Ingrese un número de teléfono válido', regex='^(\\+?56)?(\\s?)(0?9)(\\s?)[98765432]\\d{7}$')])),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleado', to=settings.AUTH_USER_MODEL)),
                ('subarea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empleados', to='usuarioApp.subarea')),
            ],
            options={
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
            },
        ),
    ]
