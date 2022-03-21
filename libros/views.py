from django.shortcuts import render
from libros.models import Libros
from libros.forms import LibrosFormulario, BusquedaLibros

# Create your views here.

def libros(request):
    listado_libros = Libros.objects.filter()
    if request.method == 'POST':
        form_libros = LibrosFormulario(request.POST)

        if form_libros.is_valid():
            data = form_libros.cleaned_data
            nuevo_libro = Libros(nombre=data['nombre'], autor=data['autor'], publicacion=data['publicacion'], genero=data['genero'])
            nuevo_libro.save()
            form_libros = LibrosFormulario()
            return render(request, 'libros.html', {'nuevo_libro':nuevo_libro,'form_libros':form_libros, 'listado_libros':listado_libros})

    form_libros = LibrosFormulario()
    return render(request, 'libros.html', {'form_libros':form_libros, 'listado_libros':listado_libros})


def buscar_libros(request):
    libros_buscados = False
    dato = request.GET.get('buscar_libro', None)
    buscador = BusquedaLibros()
    if dato is not None:
        libros_buscados = True
        libros_encontrados = Libros.objects.filter(nombre__icontains=dato)
        cant_resultados = len(libros_encontrados)
        return render(request,'buscar_libros.html',{'buscador':buscador, 'libros_encontrados':libros_encontrados, 'libros_buscados':libros_buscados,'cant_resultados':cant_resultados})


    
    return render(request,'buscar_libros.html',{'buscador':buscador})