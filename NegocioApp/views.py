from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ConsultaForm

def informaciones(request) -> HttpResponse:
    """
    Vista que muestra información sobre el negocio:
    - Quienes somos
    - Servicio al Cliente
    - Contáctanos
    
    Returns:
        HttpResponse: Página HTML renderizada con contexto
    """
    formulario = ConsultaForm(request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        messages.success(request, 'Tu consulta fue enviada correctamente.')
        return redirect('informaciones')

    context = {
        'titulo_pagina': 'Informaciones',
        'empresa': 'Ferretería Pinto',
        'telefono': '+56 9 12345678',
        'email': 'contacto@ferreteriapinto.cl',
        'direccion': 'Avenida España 123, Valparaíso, Chile',
        'formulario': formulario,
    }
    return render(request, 'informaciones.html', context)

