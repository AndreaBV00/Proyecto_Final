
from django.urls import path
from App_Artista import views
urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('Lista_Artistas/', views.lista_artistas, name='Lista_Artistas'),
    path('Detalle_Artista/', views.detalle_artista, name='Detalle_Artista'),
    path('Lista_Obras/', views.lista_obras, name='Lista_Obras'),
    path('Detalle_Obra/', views.detalle_obra, name='Detalle_Obra'),
    path('Lista_Exposiciones/', views.lista_exposiciones, name='Lista_Exposiciones'),
    path('Artista_Invitado/', views.artista_invitado, name='Artista_Invitado'),
]