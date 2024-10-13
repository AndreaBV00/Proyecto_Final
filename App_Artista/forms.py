from django import forms
from .models import Artista_invitado, Artista, Obra, Exposicion

class Artista_invitadoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    nacionalidad = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()
    texto_motivacional = forms.CharField(widget=forms.Textarea)
    link_obras = forms.URLField()
    exposicion_anfitriona = forms.ModelChoiceField(queryset=Exposicion.objects.all())
    Email_contacto = forms.EmailField()