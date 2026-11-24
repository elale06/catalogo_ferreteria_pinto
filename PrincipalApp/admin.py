from django.contrib import admin


class SuperuserAdminSite(admin.AdminSite):
	def has_permission(self, request):
		return request.user.is_active and request.user.is_superuser


admin_site = SuperuserAdminSite(name='admin')
