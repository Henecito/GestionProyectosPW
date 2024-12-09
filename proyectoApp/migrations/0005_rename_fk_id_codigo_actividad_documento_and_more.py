# Generated by Django 5.1.3 on 2024-12-09 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0005_alter_estado_modelo'),
        ('proyectoApp', '0004_remove_actividad_fk_id_estado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actividad',
            old_name='fk_id_codigo',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='actividad',
            old_name='nombre_actividad',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='documento',
            old_name='fk_id_proyecto',
            new_name='proyecto',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='fk_id_cliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='encargado_proyecto_pw',
            new_name='encargado',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='nombre_proyecto',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='encargado_proyecto_cl',
        ),
        migrations.AddField(
            model_name='actividad',
            name='estado',
            field=models.ForeignKey(blank=True, limit_choices_to={'modelo': 'Actividad'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actividades', to='baseApp.estado'),
        ),
        migrations.AddField(
            model_name='documento',
            name='estado',
            field=models.ForeignKey(blank=True, limit_choices_to={'modelo': 'Documento'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentos', to='baseApp.estado'),
        ),
        migrations.AddField(
            model_name='documento',
            name='nombre',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='estado',
            field=models.ForeignKey(blank=True, limit_choices_to={'modelo': 'Proyecto'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos', to='baseApp.estado'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='descripcion',
            field=models.TextField(max_length=200),
        ),
    ]
