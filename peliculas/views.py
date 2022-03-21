from django.http import HttpResponse
from django.shortcuts import render
from .forms import PeliculasFormulario, BusquedaPelicula
from .models import Peliculas

# Create your views here.


def peliculas(request):

    listado_peliculas = Peliculas.objects.filter()
    if request.method == 'POST':
        form_pelicula = PeliculasFormulario(request.POST)

        if form_pelicula.is_valid():
            data = form_pelicula.cleaned_data
            nueva_pelicula = Peliculas(nombre=data['nombre'], director=data['director'], año=data['año'], genero=data['genero'])
            nueva_pelicula.save()
            form_pelicula = PeliculasFormulario()
            return render(request, 'peliculas.html', {'nueva_pelicula':nueva_pelicula,'form_pelicula':form_pelicula, 'listado_peliculas':listado_peliculas})

    form_pelicula = PeliculasFormulario()
    return render(request, 'peliculas.html', {'form_pelicula':form_pelicula, 'listado_peliculas':listado_peliculas})


def buscar_peliculas(request):
    peliculas_buscadas = False
    dato = request.GET.get('buscar_pelicula', None)
    buscador = BusquedaPelicula()
    if dato is not None:
        peliculas_buscadas = True
        peliculas_encontradas = Peliculas.objects.filter(nombre__icontains=dato)
        cant_resultados = len(peliculas_encontradas)
        return render(request,'buscar_peliculas.html',{'buscador':buscador, 'peliculas_encontradas':peliculas_encontradas, 'peliculas_buscadas':peliculas_buscadas,'cant_resultados':cant_resultados})


    
    return render(request,'buscar_peliculas.html',{'buscador':buscador})