from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from proyectoApp.models import Asignar, Proyecto, Documento, Actividad
from proyectoApp.forms import AsignarForm, ProyectoForm, DocumentoForm, ActividadForm
from usuarioApp.models import Cliente, Empleado


# Resumen
@login_required
def resumenDashboard(request):
    # Conteo de los objetos
    total_proyectos = Proyecto.objects.count()  # Conteo de proyectos
    total_clientes = Cliente.objects.count()  # Conteo de clientes
    total_empleados = Empleado.objects.count()  # Conteo de empleados

    # Datos para el template
    context = {
        "total_proyectos": total_proyectos,
        "total_clientes": total_clientes,
        "total_empleados": total_empleados,
        "labels": ["Proyectos", "Clientes", "Empleados"],
        "data": [total_proyectos, total_clientes, total_empleados],
    }

    return render(request, "dashboard/resumen.html", context)


# Usando crispy forms
# Vistas para Proyecto
# @permission_required("proyectoApp.view_proyecto", login_url="/")
class ProyectoListView(PermissionRequiredMixin, ListView):
    model = Proyecto
    template_name = "proyecto/proyecto/list.html"
    permission_required = "proyectoApp.view_proyecto"
    context_object_name = "proyectos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyecto"] = self.model
        context["proyecto_verbose_name"] = self.model._meta.verbose_name
        context["proyecto_verbose_name_plural"] = self.model._meta.verbose_name_plural

        # Campos a mostrar (excluyendo id y password)
        visible_fields = [
            f for f in self.model._meta.fields if f.name not in ["id", "password"]
        ]
        context["proyecto_fields"] = visible_fields

        return context


# @permission_required("proyectoApp.add_proyecto", login_url="/")
class ProyectoCreateView(PermissionRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyecto/proyecto/form.html"
    permission_required = "proyectoApp.add_proyecto"
    success_url = reverse_lazy("proyecto-list")


# @permission_required("proyectoApp.change_proyecto", login_url="/")
class ProyectoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyecto/proyecto/form.html"
    permission_required = "proyectoApp.change_proyecto"
    success_url = reverse_lazy("proyecto-list")


# @permission_required("proyectoApp.delete_proyecto", login_url="/")
class ProyectoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Proyecto
    template_name = "proyecto/proyecto/delete.html"
    permission_required = "proyectoApp.delete_proyecto"
    success_url = reverse_lazy("proyecto-list")


# Vistas para Documento
# @permission_required("proyectoApp.view_documento", login_url="/")
class DocumentoListView(PermissionRequiredMixin, ListView):
    model = Documento
    template_name = "proyecto/documentos/list.html"
    permission_required = "proyectoApp.view_documento"
    context_object_name = "documentos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documento"] = self.model
        context["documento_verbose_name"] = self.model._meta.verbose_name
        context["documento_verbose_name_plural"] = self.model._meta.verbose_name_plural

        # Campos a mostrar (excluyendo id y password)
        visible_fields = [
            f for f in self.model._meta.fields if f.name not in ["id", "password"]
        ]
        context["documento_fields"] = visible_fields

        return context


# @permission_required("proyectoApp.add_documento", login_url="/")
class DocumentoCreateView(PermissionRequiredMixin, CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = "proyecto/documentos/form.html"
    permission_required = "proyectoApp.add_documento"
    success_url = reverse_lazy("documento-list")


# @permission_required("proyectoApp.change_documento", login_url="/")
class DocumentoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Documento
    form_class = DocumentoForm
    template_name = "proyecto/documentos/form.html"
    permission_required = "proyectoApp.change_documento"
    success_url = reverse_lazy("documento-list")


# @permission_required("proyectoApp.delete_documento", login_url="/")
class DocumentoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Documento
    template_name = "proyecto/documentos/delete.html"
    permission_required = "proyectoApp.delete_documento"
    success_url = reverse_lazy("documento-list")


# Vistas para Actividad
# @permission_required("proyectoApp.view_actividad", login_url="/")
class ActividadListView(PermissionRequiredMixin, ListView):
    model = Actividad
    template_name = "proyecto/actividad/list.html"
    permission_required = "proyectoApp.view_actividad"
    context_object_name = "actividades"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actividad"] = self.model
        context["actividad_verbose_name"] = self.model._meta.verbose_name
        context["actividad_verbose_name_plural"] = self.model._meta.verbose_name_plural

        # Campos a mostrar (excluyendo id y password)
        visible_fields = [
            f for f in self.model._meta.fields if f.name not in ["id", "password"]
        ]
        context["actividad_fields"] = visible_fields

        return context


# @permission_required("proyectoApp.add_actividad", login_url="/")
class ActividadCreateView(PermissionRequiredMixin, CreateView):
    model = Actividad
    form_class = ActividadForm
    template_name = "proyecto/actividad/form.html"
    permission_required = "proyectoApp.add_actividad"
    success_url = reverse_lazy("actividad-list")


# @permission_required("proyectoApp.change_actividad", login_url="/")
class ActividadUpdateView(PermissionRequiredMixin, UpdateView):
    model = Actividad
    form_class = ActividadForm
    template_name = "proyecto/actividad/form.html"
    permission_required = "proyectoApp.change_actividad"
    success_url = reverse_lazy("actividad-list")


# @permission_required("proyectoApp.delete_actividad", login_url="/")
class ActividadDeleteView(PermissionRequiredMixin, DeleteView):
    model = Actividad
    template_name = "proyecto/actividad/delete.html"
    permission_required = "proyectoApp.delete_actividad"
    success_url = reverse_lazy("actividad-list")

# Vista para Asignar
class AsignarListView(PermissionRequiredMixin, ListView):
    model = Asignar
    template_name = "asignar_list.html"
    permission_required = "usuarioApp.view_asignar"
    context_object_name = "asignaciones"


class AsignarCreateView(PermissionRequiredMixin, CreateView):
    model = Asignar
    form_class = AsignarForm
    template_name = "asignar_form.html"
    permission_required = "usuarioApp.add_asignar"
    success_url = reverse_lazy("asignar_list")

    def form_valid(self, form):
        messages.success(self.request, "Asignación creada exitosamente.")
        return super().form_valid(form)


class AsignarUpdateView(PermissionRequiredMixin, UpdateView):
    model = Asignar
    form_class = AsignarForm
    template_name = "asignar_form.html"
    permission_required = "usuarioApp.change_asignar"
    success_url = reverse_lazy("asignar_list")

    def form_valid(self, form):
        messages.success(self.request, "Asignación actualizada exitosamente.")
        return super().form_valid(form)


class AsignarDeleteView(PermissionRequiredMixin, DeleteView):
    model = Asignar
    template_name = "asignar_confirm_delete.html"
    permission_required = "usuarioApp.delete_asignar"
    success_url = reverse_lazy("asignar_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Asignación eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)
