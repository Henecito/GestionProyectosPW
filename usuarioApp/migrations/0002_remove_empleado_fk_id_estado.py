# Generated by Django 5.1.3 on 2024-12-03 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarioApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='fk_id_estado',
        ),
    ]