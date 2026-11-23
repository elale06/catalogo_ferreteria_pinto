from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.volumen, name='volumen'),
    path('resumen/', views.resumen, name='resumen'),
    path('acceso/', views.acceso, name='acceso'),
    path('productos/', views.listar, name='listar'),
    path('productos/crear/', views.crear, name='crear'),
    path('productos/<int:producto_id>/actualizar/', views.actualizar, name='actualizar'),
    path('productos/<int:producto_id>/eliminar/', views.eliminar, name='eliminar'),
]
