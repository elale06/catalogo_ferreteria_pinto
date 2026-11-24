from django.urls import path, include
from PrincipalApp.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('PrincipalApp.urls')),
    path('negocio/', include('NegocioApp.urls')),
    path('categorias/', include('CategoriasApp.urls')),
    path('api/', include('CategoriasApp.api_urls')),
]
