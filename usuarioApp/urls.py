from django.urls import path
from usuarioApp.views import NuevoUsuario

urlpatterns = [
    path('nuevo_usuario/', NuevoUsuario, name='nuevo_usuario'),
]

