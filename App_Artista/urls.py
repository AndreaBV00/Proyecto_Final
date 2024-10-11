
from django.urls import path
from App_Artista import views
urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('Lista_Artistas/', views.lista_artistas, name='Lista_Artistas'),
    path('Lista_Obras/', views.lista_obras, name='Lista_Obras'),
    path('Lista_Exposiciones/', views.lista_exposiciones, name='Lista_Exposiciones'),
]