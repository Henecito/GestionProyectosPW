from django.shortcuts import render
from django.contrib import messages
from proyectoApp.models import Cliente, Proyecto
from proyectoApp.forms import ClienteForm, ProyectoForm


# Proyectos
def CrearProyecto(request):
    form = ProyectoForm()
    data = {"titulo": "Crear Proyecto", "form": form}
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proyecto registrado con éxito!")
    return render(request, "proyecto/form_proyecto.html", data)


def ListarProyectos(request):
    proyectos = Proyecto.objects.all()
    data = {"lista": proyectos}
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
    return render(request, "proyecto/form_proyecto.html", {"form": form})


def EliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(pk=id)
    proyecto.delete()
    # messages.success(request, "Proyecto eliminado con éxito!")
    return render(request, "dashboard/eliminar_proyecto.html")


# Clientes
# Hay que definir bien los templates que se van a usar


def CrearCliente(request):
    form = ClienteForm()
    data = {"titulo": "Registrar Cliente", "form": form}
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente registrado con éxito!")
    return render(request, "proyecto/form_cliente.html", data)


def ListarClientes(request):
    lista = Cliente.objects.all()
    data = {"lista": lista}
    return render(request, "proyecto/listar_clientes.html", data)


def EditarCliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    form = ClienteForm(instance=cliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            # messages.success(request, "Proyecto actualizado con éxito!")
    # data = {"titulo": "Editar Proyecto", "form": form}
    return render(request, "proyecto/form_cliente.html", {"form": form})


def EliminarCliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    # messages.success(request, "Proyecto eliminado con éxito!")
    return render(request, "proyecto/eliminar_cliente.html")
