# Generated by Django 4.2 on 2024-03-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0055_activo_categoria_activo_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='activo',
            name='descripcion',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='activo',
            name='modelo',
            field=models.CharField(default='', max_length=50),
        ),
    ]