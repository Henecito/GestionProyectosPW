# Generated by Django 5.1.1 on 2024-11-26 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoApp', '0002_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.PositiveIntegerField(),
        ),
    ]
