from django.urls import path
from .views import series, buscar_series


urlpatterns = [
    path('inicio/', series, name='series'),
    path('buscador/', buscar_series, name='buscador_series'),
   
    
]