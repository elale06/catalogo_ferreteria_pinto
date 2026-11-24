from django.contrib import admin
from PrincipalApp.admin import admin_site
from .models import Precios, Volumen


@admin.register(Volumen, site=admin_site)
class VolumenAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'categoria', 'stock')
	search_fields = ('nombre', 'categoria')
	list_filter = ('categoria',)
	ordering = ('id',)


@admin.register(Precios, site=admin_site)
class PreciosAdmin(admin.ModelAdmin):
	list_display = ('volumen', 'precio', 'moneda', 'observacion')
	search_fields = ('volumen__nombre', 'volumen__categoria', 'observacion')
	list_filter = ('moneda',)
	ordering = ('volumen__id',)

