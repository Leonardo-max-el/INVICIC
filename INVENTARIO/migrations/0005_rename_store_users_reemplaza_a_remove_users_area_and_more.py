# Generated by Django 4.2 on 2024-03-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0004_alter_actaentrega_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='store',
            new_name='reemplaza_a',
        ),
        migrations.RemoveField(
            model_name='users',
            name='area',
        ),
        migrations.RemoveField(
            model_name='users',
            name='fecha_registro',
        ),
        migrations.RemoveField(
            model_name='users',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='users',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='users',
            name='name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='post',
        ),
        migrations.AddField(
            model_name='users',
            name='planilla',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='users',
            name='unidad_de_negocio',
            field=models.CharField(default='', max_length=50),
        ),
    ]