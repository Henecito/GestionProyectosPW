from django.urls import include, path
from baseApp import views

urlpatterns = [
    # Ruta para la página de login
    path('login/', views.login_view, name='login'),  # Vista de login
    
    # Rutas para las vistas del dashboard (protegidas por login_required)
    path('', views.dashboard_view, name='dashboard'),  # Página principal del Dashboard
    path('resumen/', views.resumen_view, name='resumen'),  # Página de resumen
    path('proyecto/', include('proyectoApp.urls')),  # Agregar un nuevo proyecto
    path('usuario/', include('usuarioApp.urls')),
]
