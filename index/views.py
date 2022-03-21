from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    diccionario_de_datos = {}

    return render(request, 'inicio.html', diccionario_de_datos)



