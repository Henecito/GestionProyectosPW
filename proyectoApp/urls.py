"""
URL configuration for GestionProyectosPW project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# GestionProyectosPW/urls.py
from django.contrib import admin
from django.urls import path, include
from proyectoApp import views

urlpatterns = [
    # Proyectos
    path("nuevo/", views.CrearProyecto, name="nuevo_proyecto"),
    path("lista/", views.ListarProyectos, name="listar_proyectos"),
    path("editar_proyecto/<int:codigo>/", views.EditarProyecto, name="editar_proyecto"),
    path("eliminar_proyecto/<int:codigo>/", views.EliminarProyecto, name="eliminar_proyecto"),
    # Clientes
    path("nuevo_cliente/", views.CrearCliente, name="nuevo_cliente"),
    path("lista_clientes/", views.ListarClientes, name="listar_clientes"),
    path("editar_cliente/<int:rut>/", views.EditarCliente, name="editar_cliente"),
    path("eliminar_cliente/<int:rut>/", views.EliminarCliente, name="eliminar_cliente"),
]

