# Generated by Django 4.2 on 2024-03-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0026_users_genero_adryan'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='fecha_de_ingreso',
            field=models.DateField(default='1900-01-01'),
        ),
    ]
