from django.urls import path
from .views import peliculas, buscar_peliculas


urlpatterns = [
    path('inicio/', peliculas, name='peliculas'),
    path('buscador/', buscar_peliculas, name='buscador_peliculas'),
   
    
]