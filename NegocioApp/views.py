from django.shortcuts import render
from django.http import HttpResponse

def informaciones(request) -> HttpResponse:
    """
    Vista que muestra información sobre el negocio:
    - Quienes somos
    - Servicio al Cliente
    - Contáctanos
    
    Returns:
        HttpResponse: Página HTML renderizada con contexto
    """
    context = {
        'titulo_pagina': 'Informaciones',
        'empresa': 'Ferretería Pinto',
        'telefono': '+56 9 12345678',
        'email': 'contacto@ferreteriapinto.cl',
        'direccion': 'Avenida España 123, Valparaíso, Chile'
    }
    return render(request, 'informaciones.html', context)

