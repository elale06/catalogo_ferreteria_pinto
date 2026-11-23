from django.shortcuts import render
from django.http import HttpResponse

def secciones(request) -> HttpResponse:
    context = {
        'titulo_pagina': 'Inicio',
        'descripcion': 'Bienvenido al Catálogo Ferretería Pinto'
    }
    return render(request, 'secciones.html', context)
