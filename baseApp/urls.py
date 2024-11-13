from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página de login
    path('login/', views.login_view, name='login'),  # Vista de login
    
    # Rutas para las vistas del dashboard (protegidas por login_required)
    path('', views.dashboard_view, name='dashboard'),  # Página principal del Dashboard
    path('resumen/', views.resumen_view, name='resumen'),  # Página de resumen
    path('nuevo_proyecto/', views.nuevo_proyecto_view, name='nuevo_proyecto'),  # Agregar un nuevo proyecto
    path('proyectos/', views.proyectos_view, name='proyectos'),  # Lista de proyectos
]
