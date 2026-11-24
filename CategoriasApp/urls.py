from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.volumen, name='volumen'),
    path('resumen/', views.resumen, name='resumen'),
    path('acceso/', views.acceso, name='acceso'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('productos/', views.listar, name='listar'),
    path('productos/crear/', views.crear, name='crear'),
    path('productos/<int:producto_id>/actualizar/', views.actualizar, name='actualizar'),
    path('productos/<int:producto_id>/eliminar/', views.eliminar, name='eliminar'),
]
