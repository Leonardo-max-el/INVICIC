# Generated by Django 4.2 on 2024-03-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0010_remove_users_codigo_de_personal_remove_users_local_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='sub_area_de_trabajo',
            field=models.CharField(default='', max_length=100),
        ),
    ]