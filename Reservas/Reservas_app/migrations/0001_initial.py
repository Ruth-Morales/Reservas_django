# Generated by Django 4.2.4 on 2023-12-01 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('telefono', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('comensales', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('estado', models.CharField(max_length=30)),
                ('observacion', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
