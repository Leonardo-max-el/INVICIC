# Generated by Django 4.2 on 2024-04-29 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0083_asignacionactivo_devuelto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignacionactivo',
            name='devuelto',
        ),
    ]