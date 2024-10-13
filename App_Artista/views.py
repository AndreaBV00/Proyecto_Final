from django.shortcuts import render
from django.http import HttpResponse
from .models import Artista_invitado, Artista, Obra, Exposicion
from .forms import Artista_invitadoForm

# Create your views here.
def Artista_Invitado(request):
    if request.method == 'POST':
        mi_form = Artista_invitadoForm(request.POST)
        
        if mi_form.is_valid():
            data = mi_form.cleaned_data
            nuevo_artista = Artista_invitado(
                nombre = data['nombre'],
                nacionalidad = data['nacionalidad'],
                fecha_nacimiento = data['fecha_nacimiento'],
                texto_motivacional = data['texto_motivacional'],
                link_obras = data['link_obras'],
                email_contacto = data['email_contacto'],
            )
            nuevo_artista.save()
            return HttpResponse('Gracias por enviar los datos')
        else:
            return render(request, 'Artista_Invitado.html', {'mi_form': mi_form})

    else:
        mi_form = Artista_invitadoForm()
    return render(request, 'Artista_Invitado.html', {'mi_form': mi_form})


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

