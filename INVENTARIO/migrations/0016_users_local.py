# Generated by Django 4.2 on 2024-03-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INVENTARIO', '0015_remove_users_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='local',
            field=models.CharField(default='', max_length=20),
        ),
    ]