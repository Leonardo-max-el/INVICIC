# Generated by Django 4.2 on 2024-04-13 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0074_rename_users_actaentrega_usuarios_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='activo',
            name='asignado_a',
        ),
        migrations.RemoveField(
            model_name='activo',
            name='fecha_asignacion',
        ),
    ]