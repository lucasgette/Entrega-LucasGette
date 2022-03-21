from django.urls import path
from .views import libros, buscar_libros


urlpatterns = [
    path('inicio/', libros, name='libros'),
    path('buscador/', buscar_libros, name='buscador_libros'),
   
    
]