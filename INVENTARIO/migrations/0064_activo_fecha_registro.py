# Generated by Django 4.2 on 2024-03-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0063_activo_devolucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='activo',
            name='fecha_registro',
            field=models.DateTimeField(default='1900-01-01'),
        ),
    ]
