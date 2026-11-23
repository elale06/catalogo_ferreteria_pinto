from django.contrib import admin
from .models import Precios, Volumen


@admin.register(Volumen)
class VolumenAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'categoria', 'stock')
	search_fields = ('nombre', 'categoria')
	list_filter = ('categoria',)
	ordering = ('id',)


@admin.register(Precios)
class PreciosAdmin(admin.ModelAdmin):
	list_display = ('volumen', 'precio', 'moneda', 'observacion')
	search_fields = ('volumen__nombre', 'volumen__categoria', 'observacion')
	list_filter = ('moneda',)
	ordering = ('volumen__id',)

