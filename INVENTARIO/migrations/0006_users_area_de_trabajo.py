# Generated by Django 4.2 on 2024-03-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0005_rename_store_users_reemplaza_a_remove_users_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='area_de_trabajo',
            field=models.CharField(default='', max_length=100),
        ),
    ]