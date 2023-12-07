from .models import Reserva
from . import forms
from django.shortcuts import redirect, render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def reservas(request):
    res = Reserva.objects.all()
    data = {'reser': res}
    return render(request, 'reservas.html', data)

def agregar(request):
    form = forms.FormReserva()
    if (request.method == 'POST'):
        form = forms.FormReserva(request.POST)
        if (form.is_valid()):
            form.save()
        return reservas(request)
    
    data = {'form' : form}
    return render(request, 'reservar.html', data)

def eliminar(request, id):
    pro = Reserva.objects.get(id = id)
    pro.delete()
    return redirect('/reservas')

def modificar(request, id):
    res = Reserva.objects.get(id = id)
    form = forms.FormReserva(instance=res)
    if (request.method == 'POST'):
        form = forms.FormReserva(request.POST,
                                  instance=res)
        if (form.is_valid()):
            form.save()
        return reservas(request)
    data = {'form': form}
    return render(request, 'reservar.html', data)

