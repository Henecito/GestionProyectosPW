# Generated by Django 5.1.3 on 2024-12-09 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0004_alter_estado_unique_together_estado_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='modelo',
            field=models.CharField(choices=[('Proyecto', 'Proyecto'), ('Documento', 'Documento'), ('Actividad', 'Actividad')], max_length=20),
        ),
    ]