# Generated by Django 4.2.4 on 2023-12-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservas_app', '0002_alter_reserva_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
