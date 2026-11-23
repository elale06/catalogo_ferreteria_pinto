from django.shortcuts import render
from django.http import HttpResponse

def secciones(request) -> HttpResponse:
    """
    Vista principal que muestra las secciones del catálogo de ferretería.
    Contiene enlaces a Negocio y Categorías.
    
    Returns:
        HttpResponse: Página HTML renderizada con contexto
    """
    context = {
        'titulo_pagina': 'Inicio',
        'descripcion': 'Bienvenido al Catálogo Ferretería Pinto'
    }
    return render(request, 'secciones.html', context)

