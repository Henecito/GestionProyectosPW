from django.urls import path
from proyectoApp import views

urlpatterns = [
    path("resumen/", views.resumenDashboard, name="resumen"),
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
    # Crispy forms
    # Proyectos
    path("proyecto/", views.ProyectoListView.as_view(), name="proyecto-list"),
    path("proyecto/nuevo/", views.ProyectoCreateView.as_view(), name="proyecto-create"),
    path(
        "proyecto/editar/<int:pk>/",
        views.ProyectoUpdateView.as_view(),
        name="proyecto-update",
    ),
    path(
        "proyecto/eliminar/<int:pk>/",
        views.ProyectoDeleteView.as_view(),
        name="proyecto-delete",
    ),
    # Documentos
    path("documento/", views.DocumentoListView.as_view(), name="documento-list"),
    path(
        "documento/nuevo/", views.DocumentoCreateView.as_view(), name="documento-create"
    ),
    path(
        "documento/editar/<str:pk>/",
        views.DocumentoUpdateView.as_view(),
        name="documento-update",
    ),
    path(
        "documento/eliminar/<str:pk>/",
        views.DocumentoDeleteView.as_view(),
        name="documento-delete",
    ),
    # Actividades
    path("actividad/", views.ActividadListView.as_view(), name="actividad-list"),
    path(
        "actividad/nuevo/", views.ActividadCreateView.as_view(), name="actividad-create"
    ),
    path(
        "actividad/editar/<int:pk>/",
        views.ActividadUpdateView.as_view(),
        name="actividad-update",
    ),
    path(
        "actividad/eliminar/<int:pk>/",
        views.ActividadDeleteView.as_view(),
        name="actividad-delete",
    ),
]
