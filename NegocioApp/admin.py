from django.contrib import admin
from PrincipalApp.admin import admin_site
from .models import Consulta


@admin.register(Consulta, site=admin_site)
class ConsultaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'email', 'telefono', 'asunto', 'creada_en')
	list_filter = ('creada_en',)
	search_fields = ('nombre', 'email', 'telefono', 'asunto', 'mensaje')
	readonly_fields = ('nombre', 'email', 'telefono', 'asunto', 'mensaje', 'creada_en')
	date_hierarchy = 'creada_en'

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False
