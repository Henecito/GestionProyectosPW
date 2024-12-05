from django.urls import path
from . import views

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
    path('usuarios/', views.UserListView.as_view(), name='lista_usuarios'),
    path('usuarios/perfil/cambiar-contrasena/', views.PasswordChangeView.as_view(), name='password_change'),
]
