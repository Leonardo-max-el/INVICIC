# Generated by Django 4.2 on 2024-04-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0075_rename_users_user_remove_activo_asignado_a_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actaentrega',
            old_name='usuarios',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='user',
            name='activo',
        ),
        migrations.AddField(
            model_name='user',
            name='activo',
            field=models.ManyToManyField(related_name='usuarios', to='INVENTARIO.activo'),
        ),
    ]