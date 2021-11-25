from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from apps.core.models import *

# def index(request):
#     return redirect('/agenda/')

def evento(request, evento):
    eventos = Evento.objects.get()
    evento = eventos.titulo
    return HttpResponse('<h1>Local do evento: {}</h1>' .format(evento))

def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.all()
    dados = {'eventos':eventos}
    return render (request, 'agenda.html', dados)