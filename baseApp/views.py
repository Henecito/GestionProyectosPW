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


# @permission_required("baseApp.add_estado", login_url="/")
def crearEstado(request):
    form = EstadoForm()  # Cambia esto de 'Estado()' a 'EstadoForm()'
    data = {"titulo": "Crear Estado", "form": form, "ruta": "estados"}
    if request.method == "POST":
        form = EstadoForm(request.POST)  # Usa 'EstadoForm' también aquí
        if form.is_valid():
            form.save()
            messages.success(request, "Estado creado con éxito!!!")
            return redirect('estados')  # Redirige al listado de estados después de guardar
    return render(request, "base/estado/form.html", data)


# @permission_required("baseApp.change_estado", login_url="/")
def editarEstado(request, id):
    item = Estado.objects.get(pk=id)
    form = EstadoForm(instance=item)
    if request.method == "POST":
        form = EstadoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Estado editado con éxito")
            return redirect('estados')  # Redirige después de guardar para evitar reenvíos al refrescar

    data = {"titulo": "Editar Estado", "form": form, "ruta": "estados"}
    return render(request, "base/estado/form.html", data)

# @permission_required("baseApp.delete_estado", login_url="/")
def eliminarEstado(request, id):
    item = Estado.objects.get(pk=id)
    item.delete()
    return redirect("/proyecto/estados")


# @permission_required("baseApp.view_estado", login_url="/")
def listarEstado(request):
    estados = Estado.objects.all()
    paginator = Paginator(estados, 10)  # Show 10 states per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"lista": page_obj}
    return render(request, "base/estado/list.html", data)
