# Generated by Django 5.0.2 on 2024-12-05 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
        ('proyectoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fk_id_estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='baseApp.estado'),
        ),
    ]
