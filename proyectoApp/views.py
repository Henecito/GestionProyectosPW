from django.shortcuts import render
from django.contrib import messages
from proyectoApp.models import Proyecto
from proyectoApp.forms import ProyectoForm


# Proyectos
def CrearProyecto(request):
    form = ProyectoForm()
    # data = {"titulo": "Crear Proyecto", "form": form}
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Proyecto registrado con éxito!")
    return render(request, "proyecto/crear_proyecto.html", {"form": form})


def ListarProyectos(request):
    proyectos = Proyecto.objects.all()
    data = {"proyectos": proyectos}
    return render(request, "proyecto/listar_proyectos.html", data)


def EditarProyecto(request, id):
    proyecto = Proyecto.objects.get(pk=id)
    form = ProyectoForm(instance=proyecto)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            # messages.success(request, "Proyecto actualizado con éxito!")
    # data = {"titulo": "Editar Proyecto", "form": form}
    return render(request, "proyecto/editar_proyecto.html", {"form": form})


def EliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(pk=id)
    proyecto.delete()
    # messages.success(request, "Proyecto eliminado con éxito!")
    return render(request, "proyecto/eliminar_proyecto.html")
