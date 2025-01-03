from django.urls import path
from usuarioApp import views

urlpatterns = [
    # Urls para Área
    path("areas/", views.AreaListView.as_view(), name="area_list"),
    path("areas/crear/", views.AreaCreateView.as_view(), name="area_crear"),
    path("areas/editar/<int:pk>/", views.AreaUpdateView.as_view(), name="area_editar"),
    path(
        "areas/eliminar/<int:pk>/", views.AreaDeleteView.as_view(), name="area_eliminar"
    ),
    # Urls para SubÁrea
    path("subareas/", views.SubAreaListView.as_view(), name="subarea_list"),
    path("subareas/crear/", views.SubAreaCreateView.as_view(), name="subarea_crear"),
    path(
        "subareas/editar/<int:pk>/",
        views.SubAreaUpdateView.as_view(),
        name="subarea_editar",
    ),
    path(
        "subareas/eliminar/<int:pk>/",
        views.SubAreaDeleteView.as_view(),
        name="subarea_eliminar",
    ),
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
    # Urls para Empleado
    path("empleados/", views.EmpleadoListView.as_view(), name="empleado_list"),
    path("empleados/crear/", views.EmpleadoCreateView.as_view(), name="empleado_crear"),
    path(
        "empleados/editar/<str:pk>/",
        views.EmpleadoUpdateView.as_view(),
        name="empleado_editar",
    ),
    path(
        "empleados/eliminar/<str:pk>/",
        views.EmpleadoDeleteView.as_view(),
        name="empleado_eliminar",
    ),
    path("usuarios/", views.UserListView.as_view(), name="lista_usuarios"),
    path(
        "usuarios/perfil/cambiar-contrasena/",
        views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path("asignar-grupos/<int:user_id>/", views.asignar_grupos, name="asignar_grupos"),
]
