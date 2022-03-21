from django.shortcuts import render
from .models import Series
from .forms import SeriesFormulario, BusquedaSeries

# Create your views here.

def series(request):    
    listado_series = Series.objects.filter()
    if request.method == 'POST':
        form_series = SeriesFormulario(request.POST)

        if form_series.is_valid():
            data = form_series.cleaned_data
            nueva_serie = Series(nombre=data['nombre'], año=data['año'], temporadas=data['temporadas'], genero=data['genero'])
            nueva_serie.save()
            form_series = SeriesFormulario()
            return render(request, 'series.html', {'nueva_serie':nueva_serie,'form_series':form_series, 'listado_series':listado_series})

    form_series = SeriesFormulario()
    return render(request, 'series.html', {'form_series':form_series, 'listado_series':listado_series})


def buscar_series(request):
    series_buscadas = False
    dato = request.GET.get('buscar_serie', None)
    buscador = BusquedaSeries()
    if dato is not None:
        series_buscadas = True
        series_encontradas = Series.objects.filter(nombre__icontains=dato)
        cant_resultados = len(series_encontradas)
        return render(request,'buscar_series.html', {'buscador':buscador, 'series_encontradas':series_encontradas, 'series_buscadas':series_buscadas,'cant_resultados':cant_resultados})


    
    return render(request,'buscar_series.html', {'buscador':buscador})


