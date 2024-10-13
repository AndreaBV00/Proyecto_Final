from django.shortcuts import render
from django.http import HttpResponse
from .models import Artista_invitado, Artista, Obra, Exposicion

# Create your views here.
def Artista_Invitado(request):
    return render(request, 'Artista_invitado.html', {})

def Inicio(request):
    return render(request, 'Inicio.html', {})
                  
def Lista_Artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'Lista_Artistas.html', {})

def Detalle_Artista(request, id):
    artista = Artista.objects.get(id=id)
    return render(request, 'Detalle_artistas.html', {})

def Lista_Obras(request):
    obras = Obra.objects.all()
    return render(request, 'Lista_obras.html', {})

def Detalle_Obra(request, id):
    obra = Obra.objects.get(id=id)
    return render(request, 'Detalle_Obras.html', {})

def Lista_Exposiciones(request):
    exposiciones = Exposicion.objects.all()
    return render(request, 'Lista_Exposiciones.html', {})