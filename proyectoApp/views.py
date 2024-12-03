from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from proyectoApp.models import Cliente, Proyecto, Documento, Actividad
from proyectoApp.forms import ClienteForm, ProyectoForm, DocumentoForm, ActividadForm
from django.contrib.auth.decorators import login_required, permission_required


# Cliente
# Vista para Cliente
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "proyecto/clientes/cliente_list.html"
    context_object_name = "clientes"


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "proyecto/clientes/cliente_form.html"
    success_url = reverse_lazy("cliente_list")

    def form_valid(self, form):
        messages.success(self.request, "Cliente creado exitosamente.")
        return super().form_valid(form)


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "proyecto/clientes/cliente_form.html"
    success_url = reverse_lazy("cliente_list")

    def form_valid(self, form):
        messages.success(self.request, "Cliente actualizado exitosamente.")
        return super().form_valid(form)


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = "proyecto/clientes/cliente_confirm_delete.html"
    success_url = reverse_lazy("cliente_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Cliente eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)


# ----- Proyecto -----


@permission_required("proyectoApp.add_proyecto", login_url="/")
def crearProyecto(request):
    form = Proyecto()
    data = {"titulo": "Crear Proyecto", "formulario": form, "ruta": "proyectos"}
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proyectos creado con éxito!!!")
    return render(request, "proyecto/proyecto/createProyecto.html", data)


@permission_required("proyectoApp.view_proyecto", login_url="/")
def listarProyecto(request):
    proyectos = Proyecto.objects.all()
    data = {"lista": proyectos}
    return render(request, "proyecto/proyecto/proyecto.html", data)


@permission_required("proyectoApp.change_proyecto", login_url="/")
def actualizarProyecto(request, id):
    item = Proyecto.objects.get(pk=id)
    form = ProyectoForm(instance=item)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Proyecto editado con éxito")
    data = {"titulo": "Editar Proyecto", "formulario": form, "ruta": "proyectos"}
    return render(request, "proyecto/proyecto/createProyecto.html", data)


@permission_required("proyectoApp.delete_proyecto", login_url="/")
def eliminarProyecto(request, id):
    item = Proyecto.objects.get(pk=id)
    item.delete()
    return redirect("proyecto/proyecto/proyectos")


# ----- Documento -----

@permission_required("proyectoApp.add_documento", login_url="/")
def crearDocumento(request):
    form = Documento()
    data = {"titulo": "Crear Documento", "formulario": form, "ruta": "documentos"}
    if request.method == "POST":
        form = DocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Documento creado con éxito!")
            return redirect("documento_list")
    return render(request, "proyecto/documentos/createDocumento.html", data)

@permission_required("proyectoApp.view_documento", login_url="/")
def listarDocumento(request):
    documentos = Documento.objects.all()
    data = {"lista": documentos}
    return render(request, "proyecto/documentos/documento.html", data)

@permission_required("proyectoApp.change_documento", login_url="/")
def actualizarDocumento(request, codigo):
    item = Documento.objects.get(pk=codigo)
    form = DocumentoForm(instance=item)
    if request.method == "POST":
        form = DocumentoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Documento editado con éxito")
            return redirect("documento_list")
    data = {"titulo": "Editar Documento", "formulario": form, "ruta": "documentos"}
    return render(request, "proyecto/documentos/createDocumento.html", data)

@permission_required("proyectoApp.delete_documento", login_url="/")
def eliminarDocumento(request, id):
    item = Documento.objects.get(pk=id)
    item.delete()
    messages.success(request, "Documento eliminado con éxito.")
    return redirect("documento_list")



# ----- Actividad -----

@permission_required("proyectoApp.add_actividad", login_url="/")
def crearActividad(request):
    form = Actividad()
    data = {"titulo": "Crear Actividad", "formulario": form, "ruta": "actividades"}
    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Actividad creada con éxito!")
            return redirect("actividad_list")
    return render(request, "proyecto/actividad/createActivity.html", data)

@permission_required("proyectoApp.view_actividad", login_url="/")
def listarActividad(request):
    actividades = Actividad.objects.all()
    data = {"lista": actividades}
    return render(request, "proyecto/actividad/actividad.html", data)

@permission_required("proyectoApp.change_actividad", login_url="/")
def actualizarActividad(request, id):
    item = Actividad.objects.get(pk=id)
    form = ActividadForm(instance=item)
    if request.method == "POST":
        form = ActividadForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Actividad editada con éxito")
            return redirect("actividad_list")
    data = {"titulo": "Editar Actividad", "formulario": form, "ruta": "actividades"}
    return render(request, "proyecto/actividad/createActivity.html", data)

@permission_required("proyectoApp.delete_actividad", login_url="/")
def eliminarActividad(request, id):
    item = Actividad.objects.get(pk=id)
    item.delete()
    messages.success(request, "Actividad eliminada con éxito.")
    return redirect("actividad_list")
