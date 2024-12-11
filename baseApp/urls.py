from django.urls import include, path
from baseApp import views

urlpatterns = [
    path("", views.inicio, name="inicio"),  # Página principal del Dashboard
    path("proyecto/", include("proyectoApp.urls")),
    path("usuario/", include("usuarioApp.urls")),
    # Estado
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
    # Grupos y permisos
    path("grupos/", views.manage_groups, name="manage_groups"),
    # path('grupos/lista/', views.view_groups, name='view_groups'),
    path('grupos/<int:group_id>/delete/', views.delete_group, name='delete_group'),
]
