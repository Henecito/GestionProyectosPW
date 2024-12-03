from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from baseApp.forms import EstadoForm
from baseApp.models import Estado


# Vista principal
@login_required
def inicio(request):
    return render(request, "index.html")


@permission_required("proyectoApp.add_estado", login_url="/")
def crearEstado(request):
    form = Estado()
    data = {"titulo": "Crear Estado", "formulario": form, "ruta": "estados"}
    if request.method == "POST":
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estado creado con éxito!!!")
    return render(request, "proyecto/createProyecto.html", data)


@permission_required("proyectoApp.change_estado", login_url="/")
def actualizarEstado(request, id):
    item = Estado.objects.get(pk=id)
    form = EstadoForm(instance=item)
    if request.method == "POST":
        form = EstadoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Estado editado con éxito")
    data = {"titulo": "Editar Estado", "formulario": form, "ruta": "estados"}
    return render(request, "proyecto/createProyecto.html", data)


@permission_required("proyectoApp.delete_estado", login_url="/")
def eliminarEstado(request, id):
    item = Estado.objects.get(pk=id)
    item.delete()
    return redirect("/proyecto/estados")


@permission_required("proyectoApp.view_estado", login_url="/")
def listarEstado(request):
    estados = Estado.objects.all()
    data = {"lista": estados}
    return render(request, "proyecto/estado.html", data)
