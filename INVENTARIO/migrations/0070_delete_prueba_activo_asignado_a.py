# Generated by Django 4.2 on 2024-04-09 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0069_alter_activo_hostname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='prueba',
        ),
        migrations.AddField(
            model_name='activo',
            name='asignado_a',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activos_asignados', to='INVENTARIO.users'),
        ),
    ]
