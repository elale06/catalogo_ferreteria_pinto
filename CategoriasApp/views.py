from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from decimal import Decimal

from .forms import PreciosForm, VolumenForm
from .models import Precios, Volumen

def volumen(request) -> HttpResponse:
    """
    Vista que muestra el listado completo de productos desde el archivo JSON.
    """
    productos = _productos_con_precio()
    
    context = {
        'productos': productos,
        'titulo_pagina': 'Catálogo de Productos'
    }
    
    return render(request, 'volumen.html', context)


def resumen(request) -> HttpResponse:
    """
    Vista que muestra un resumen calculado de los productos:
    - Total de registros
    - Total de productos disponibles (con stock > 0)
    - Destaca visualmente los productos sin stock
    """
    productos = _productos_con_precio()
    
    # Calcular valor total para cada producto
    for producto in productos:
        producto['valor_total'] = (
            producto['precio'] * producto['stock']
            if producto['tiene_precio']
            else 0
        )
    
    # Calcular resumen
    total_registros = len(productos)
    productos_disponibles = len([p for p in productos if p.get('stock', 0) > 0])
    productos_sin_stock = len([p for p in productos if p.get('stock', 0) == 0])
    stock_total = sum(p.get('stock', 0) for p in productos)
    valor_inventario = sum(p.get('valor_total', 0) for p in productos)
    
    context = {
        'titulo_pagina': 'Resumen de Productos',
        'productos': productos,
        'total_registros': total_registros,
        'productos_disponibles': productos_disponibles,
        'productos_sin_stock': productos_sin_stock,
        'stock_total': stock_total,
        'valor_inventario': valor_inventario
    }
    
    return render(request, 'resumen.html', context)


def acceso(request) -> HttpResponse:
    """Panel para listar y gestionar los productos registrados."""
    return render(request, 'acceso.html', {'productos': _productos_con_precio()})


def listar(request) -> HttpResponse:
    return render(request, 'listar.html', {'productos': _productos_con_precio()})


def crear(request) -> HttpResponse:
    formulario = VolumenForm(request.POST or None)
    formulario_precio = PreciosForm(request.POST or None)
    if request.method == 'POST' and formulario.is_valid() and formulario_precio.is_valid():
        # corrección: ahora se utiliza transaction.atomic() para asegurar que ambas operaciones de guardado se realicen de manera atómica
        with transaction.atomic():
            producto = formulario.save()
            if formulario_precio.cleaned_data.get('precio') is not None:
                precio = formulario_precio.save(commit=False)
                precio.volumen = producto
                precio.save()
        messages.success(request, 'Producto creado correctamente.')
        return redirect('categorias:acceso')
    return render(request, 'crear.html', {'formulario': formulario, 'formulario_precio': formulario_precio})


def actualizar(request, producto_id) -> HttpResponse:
    producto = get_object_or_404(Volumen, pk=producto_id)
    formulario = VolumenForm(request.POST or None, instance=producto)
    formulario_precio = PreciosForm(request.POST or None, instance=getattr(producto, 'precio', None))
    if request.method == 'POST' and formulario.is_valid() and formulario_precio.is_valid():
        formulario.save()
        if formulario_precio.cleaned_data.get('precio') is not None:
            precio = formulario_precio.save(commit=False)
            precio.volumen = producto
            precio.save()
        elif hasattr(producto, 'precio'):
            producto.precio.delete()
        messages.success(request, 'Producto actualizado correctamente.')
        return redirect('categorias:acceso')
    return render(request, 'actualizar.html', {'formulario': formulario, 'formulario_precio': formulario_precio, 'producto': producto})


def eliminar(request, producto_id) -> HttpResponse:
    producto = get_object_or_404(Volumen, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('categorias:acceso')
    return render(request, 'eliminar.html', {'producto': producto})


def _productos_con_precio():
    """Combina el inventario con el precio editable desde el admin."""
    productos = []
    for producto in Volumen.objects.select_related('precio').order_by('id'):
        precio = getattr(producto, 'precio', None)
        productos.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'categoria': producto.categoria,
            'stock': int(producto.stock),
            'tiene_precio': precio is not None,
            'precio': Decimal(precio.precio) if precio is not None else None,
            'moneda': precio.moneda if precio is not None else None,
            'observacion': precio.observacion if precio is not None else '',
        })
    return productos

