# Generated by Django 4.2 on 2024-04-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0068_remove_activo_campus_alter_activo_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo',
            name='hostname',
            field=models.CharField(default='hs', max_length=50),
        ),
    ]
