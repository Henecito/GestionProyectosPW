# Generated by Django 5.1.3 on 2024-12-10 21:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarioApp', '0003_alter_empleado_fk_id_subarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='contacto_emergencia',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Ingrese un número de teléfono válido', regex='^(\\+?56)?(\\s?)(0?9)(\\s?)[98765432]\\d{7}$')]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Ingrese un número de teléfono válido', regex='^(\\+?56)?(\\s?)(0?9)(\\s?)[98765432]\\d{7}$')]),
        ),
    ]
