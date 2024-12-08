from django.urls import include, path
from baseApp import views

urlpatterns = [
    # Ruta para la página de login
    # path('login/', views.login_view, name='login'),  # Vista de login
    # Rutas para las vistas del dashboard (protegidas por login_required)
    path("", views.inicio, name="inicio"),  # Página principal del Dashboard
    path("proyecto/", include("proyectoApp.urls")),
    path("usuario/", include("usuarioApp.urls")),
    # ----- Estado -----
    path("estados/", views.gestionar_estados, name="gestionar_estados"),
    path(
        "estados/editar/<int:estado_id>/",
        views.gestionar_estados,
        name="gestionar_estados_editar",
    ),
    path(
        "estados/eliminar/<int:estado_id>/",
        views.eliminar_estado,
        name="eliminar_estado",
    ),
]
