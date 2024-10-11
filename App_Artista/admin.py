from django.contrib import admin
from .models import Artista_invitado, Artista, Obra, Exposicion 

# Register your models here.
admin.register(Artista_invitado)

admin.register(Artista)

admin.register(Obra)

admin.register(Exposicion)
