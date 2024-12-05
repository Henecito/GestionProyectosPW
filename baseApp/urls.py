from django.urls import include, path
from baseApp import views

urlpatterns = [
    # Ruta para la página de login
    # path('login/', views.login_view, name='login'),  # Vista de login
    # Rutas para las vistas del dashboard (protegidas por login_required)
    path("", views.inicio, name="inicio"),  # Página principal del Dashboard
    path('proyecto/', include('proyectoApp.urls')),
    path('usuario/', include('usuarioApp.urls')),
    # ----- Estado -----
    path("crearestado/", views.crearEstado, name="crearEstado"),
    path("estados/", views.listarEstado, name="estados"),
    path("actualizarEstado/<int:id>", views.editarEstado, name="actualizarEstado"),
    path("eliminarestado/<int:id>", views.eliminarEstado, name="eliminarEstado"),
]
