from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PrincipalApp.urls')),
    path('negocio/', include('NegocioApp.urls')),
    path('categorias/', include('CategoriasApp.urls')),
    path('api/', include('CategoriasApp.api_urls')),
]
