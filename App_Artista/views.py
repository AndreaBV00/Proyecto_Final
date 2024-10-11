from django.shortcuts import render
from django.http import HttpResponse
from .models import Artista_invitado, Artista, Obra, Exposicion

# Create your views here.
def artista_invitado(request, nombre, nacionalidad, fecha_nacimiento, texto_motivacional, link_obras, exposicion_anfitriona, Email_contacto):
    nuevo_artista = Artista_invitado(nombre=nombre, nacionalidad=nacionalidad, fecha_nacimiento=fecha_nacimiento, texto_motivacional=texto_motivacional, link_obras=link_obras, exposicion_anfitriona=exposicion_anfitriona, Email_contacto=Email_contacto)
    artista_invitado.save()
    return HttpResponse(f'Artista invitado creado: {nuevo_artista.nombre}, nos comunicaremos a la brevedad con novedades sobre la exposición')

def inicio(request):
    return render(request, 'inicio.html')

def lista_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'lista_artistas.html', {'artistas': artistas})

def detalle_artista(request, id):
    artista = Artista.objects.get(id=id)
    return render(request, 'detalle_artista.html', {'artista': artista})

def lista_obras(request):
    obras = Obra.objects.all()
    return render(request, 'lista_obras.html', {'obras': obras})

def detalle_obra(request, id):
    obra = Obra.objects.get(id=id)
    return render(request, 'detalle_obra.html', {'obra': obra})

def lista_exposiciones(request):
    exposiciones = Exposicion.objects.all()
    return render(request, 'lista_exposiciones.html', {'exposiciones': exposiciones, 'exposiciones': id})