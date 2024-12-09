from django.urls import path
from proyectoApp import views
from .views import resumenDashboard

urlpatterns = [
    path("resumen/", resumenDashboard, name="resumen"),
    # Cliente
    path("clientes/", views.ClienteListView.as_view(), name="cliente_list"),
    path("clientes/crear/", views.ClienteCreateView.as_view(), name="cliente_crear"),
    path(
        "clientes/editar/<str:pk>/",
        views.ClienteUpdateView.as_view(),
        name="cliente_editar",
    ),
    path(
        "clientes/eliminar/<str:pk>/",
        views.ClienteDeleteView.as_view(),
        name="cliente_eliminar",
    ),
    # Proyecto
    path("crearproyecto/", views.crearProyecto, name="crearproyecto"),
    path("proyectos/", views.listarProyecto, name="proyectos"),
    path("editarproyecto/<int:id>", views.actualizarProyecto, name="editarproyecto"),
    path("eliminarproyecto/<int:id>", views.eliminarProyecto, name="eliminarproyecto"),
    # Documento
    path("creardocumento/", views.crearDocumento, name="creardocumento"),
    path("listardocumentos/", views.listarDocumento, name="listardocumentos"),
    path(
        "editardocumento/<int:codigo>",
        views.actualizarDocumento,
        name="editardocumento",
    ),
    path(
        "eliminardocumento/<int:codigo>",
        views.eliminarDocumento,
        name="eliminardocumento",
    ),
    # Actividad
    path("crearactividad/", views.crearActividad, name="crearactividad"),
    path("actividades/", views.listarActividad, name="actividades"),
    path("editaractividad/<int:id>", views.actualizarActividad, name="editaractividad"),
    path(
        "eliminaractividad/<int:id>", views.eliminarActividad, name="eliminaractividad"
    ),
]
