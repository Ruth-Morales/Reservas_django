from django import forms
from . import models


class FormReserva(forms.ModelForm):
    ESTADOS=[('reservada', 'RESERVADA'), ('completada', 'COMPLETADA'), ('anulada', 'ANULADA'), ('no asisten', 'NO ASISTEN')]
    nombre = forms.CharField(min_length=3, max_length=80)
    telefono = forms.IntegerField()
    fecha = forms.DateTimeField()
    comensales = forms.IntegerField(min_value=1, max_value=15)
    email = forms.CharField(widget=forms.EmailInput)
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    observacion = forms.CharField(required=False)

    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control' 
    fecha.widget.attrs['class'] = 'form-control'
    comensales.widget.attrs['class'] = 'form-control' 
    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select'
    observacion.widget.attrs['class'] = 'form-control'

    telefono.widget.attrs['placeholders']= 'hola'


    class Meta:
        model = models.Reserva
        fields = '__all__'




