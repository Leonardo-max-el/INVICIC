# Generated by Django 4.2 on 2024-03-07 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0031_users_jefe_inmediato_jerarquico'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='INVENTARIO.store'),
        ),
        migrations.AlterField(
            model_name='users',
            name='jefe_inmediato_jerarquico',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='reemplaza_a',
            field=models.CharField(default='', max_length=100),
        ),
    ]