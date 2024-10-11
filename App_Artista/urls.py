
from django.urls import path
from App_Artista import views
urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('Lista_Artistas/', views.Lista_Artistas, name='Lista_Artistas'),
    path('Lista_Obras/', views.Lista_Obras, name='Lista_Obras'),
    path('Lista_Exposiciones/', views.Lista_Exposiciones, name='Lista_Exposiciones'),
]