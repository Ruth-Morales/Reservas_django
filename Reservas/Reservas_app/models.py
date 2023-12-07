from django.db import models

# Create your models here.

class Reserva(models.Model):
    nombre = models.CharField(max_length=80)
    telefono = models.IntegerField()
    fecha = models.DateTimeField()
    comensales = models.IntegerField()
    email = models.EmailField()
    estado = models.CharField(max_length=30)
    observacion = models.CharField(max_length=250, null=True)


