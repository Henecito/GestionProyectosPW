from django.urls import path
from proyectoApp import views

urlpatterns = [
    path("resumen/", views.resumenDashboard, name="resumen"),
    
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
    path('actividad/<int:pk>/update-encargado/', 
         views.ActividadUpdateViewEncargado.as_view(), 
         name='actividad-update-encargado'),
]
