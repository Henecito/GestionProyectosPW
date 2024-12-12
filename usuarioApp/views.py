from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    View,
)

from usuarioApp.models import Area, Cliente, SubArea, Empleado
from usuarioApp.forms import (
    AreaForm,
    ClienteForm,
    SubAreaForm,
    EmpleadoForm,
    PasswordChangeFormCustom,
    AsignarGruposForm,
)


# Vista para Área
class AreaListView(PermissionRequiredMixin, ListView):
    model = Area
    template_name = "usuario/area/area_list.html"
    permission_required = "usuarioApp.view_area"
    context_object_name = "areas"


class AreaCreateView(PermissionRequiredMixin, CreateView):
    model = Area
    form_class = AreaForm
    template_name = "usuario/area/area_form.html"
    permission_required = "usuarioApp.add_area"
    success_url = reverse_lazy("area_list")

    def form_valid(self, form):
        messages.success(self.request, "Área creada exitosamente.")
        return super().form_valid(form)


class AreaUpdateView(PermissionRequiredMixin, UpdateView):
    model = Area
    form_class = AreaForm
    template_name = "usuario/area/area_form.html"
    permission_required = "usuarioApp.change_area"
    success_url = reverse_lazy("area_list")

    def form_valid(self, form):
        messages.success(self.request, "Área actualizada exitosamente.")
        return super().form_valid(form)


class AreaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Area
    template_name = "usuario/area/area_confirm_delete.html"
    permission_required = "usuarioApp.delete_area"
    success_url = reverse_lazy("area_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Área eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)


# Vista para SubÁrea
class SubAreaListView(PermissionRequiredMixin, ListView):
    model = SubArea
    template_name = "usuario/area/subarea/subarea_list.html"
    permission_required = "usuarioApp.view_subarea"
    context_object_name = "subareas"


class SubAreaCreateView(PermissionRequiredMixin, CreateView):
    model = SubArea
    form_class = SubAreaForm
    template_name = "usuario/area/subarea/subarea_form.html"
    permission_required = "usuarioApp.add_subarea"
    success_url = reverse_lazy("subarea_list")

    def form_valid(self, form):
        messages.success(self.request, "SubÁrea creada exitosamente.")
        return super().form_valid(form)


class SubAreaUpdateView(PermissionRequiredMixin, UpdateView):
    model = SubArea
    form_class = SubAreaForm
    template_name = "usuario/area/subarea/subarea_form.html"
    permission_required = "usuarioApp.change_subarea"
    success_url = reverse_lazy("subarea_list")

    def form_valid(self, form):
        messages.success(self.request, "SubÁrea actualizada exitosamente.")
        return super().form_valid(form)


class SubAreaDeleteView(PermissionRequiredMixin, DeleteView):
    model = SubArea
    template_name = "usuario/area/subarea/subarea_confirm_delete.html"
    permission_required = "usuarioApp.delete_subarea"
    success_url = reverse_lazy("subarea_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "SubÁrea eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)


# Cliente
# @permission_required("proyectoApp.view_cliente", login_url="/")
class ClienteListView(PermissionRequiredMixin, ListView):
    model = Cliente
    template_name = "proyecto/clientes/list.html"
    permission_required = "proyectoApp.view_cliente"
    context_object_name = "clientes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Campos a mostrar (excluyendo id y password)
        visible_fields = [f for f in self.model._meta.fields]
        context["cliente_fields"] = visible_fields
        return context


# @permission_required("proyectoApp.add_cliente", login_url="/")
class ClienteCreateView(PermissionRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "proyecto/clientes/form.html"
    permission_required = "proyectoApp.add_cliente"
    success_url = reverse_lazy("cliente_list")

    def form_valid(self, form):
        messages.success(self.request, "Cliente creado exitosamente.")
        return super().form_valid(form)


# @permission_required("proyectoApp.update_cliente", login_url="/")
class ClienteUpdateView(PermissionRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "proyecto/clientes/form.html"
    permission_required = "proyectoApp.change_cliente"
    success_url = reverse_lazy("cliente_list")

    def form_valid(self, form):
        messages.success(self.request, "Cliente actualizado exitosamente.")
        return super().form_valid(form)


# @permission_required("proyectoApp.delete_cliente", login_url="/")
class ClienteDeleteView(PermissionRequiredMixin, DeleteView):
    model = Cliente
    template_name = "proyecto/clientes/delete.html"
    permission_required = "proyectoApp.delete_cliente"
    success_url = reverse_lazy("cliente_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Cliente eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)


# Vista para Empleado
class EmpleadoListView(PermissionRequiredMixin, ListView):
    model = Empleado
    template_name = "usuario/empleados/empleado_list.html"
    permission_required = "usuarioApp.view_empleado"
    context_object_name = "empleados"


class EmpleadoCreateView(PermissionRequiredMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "usuario/empleados/empleado_form.html"
    permission_required = "usuarioApp.add_empleado"
    success_url = reverse_lazy("empleado_list")

    def form_valid(self, form):
        messages.success(self.request, "Empleado creado exitosamente.")
        return super().form_valid(form)


class EmpleadoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "usuario/empleados/empleado_form.html"
    permission_required = "usuarioApp.change_empleado"
    success_url = reverse_lazy("empleado_list")

    def form_valid(self, form):
        messages.success(self.request, "Empleado actualizado exitosamente.")
        return super().form_valid(form)


class EmpleadoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Empleado
    template_name = "usuario/empleados/empleado_confirm_delete.html"
    permission_required = "usuarioApp.delete_empleado"
    success_url = reverse_lazy("empleado_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Empleado eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)


class UserListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = "usuario/usuarios/lista_usuarios.html"
    permission_required = "auth.view_user"
    context_object_name = "usuarios"


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeFormCustom  # Tu formulario personalizado
    template_name = "usuario/perfil/password_change_form.html"
    success_url = reverse_lazy(
        "password_change"
    )  # Redirigir a la página de inicio tras un cambio exitoso

    def form_valid(self, form):
        # Guardar la nueva contraseña
        user = form.save()

        # Actualizar la sesión para que el usuario no se desloguee tras cambiar la contraseña
        update_session_auth_hash(self.request, user)

        # Mostrar mensaje de éxito
        messages.success(self.request, "Contraseña cambiada exitosamente.")

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


# Grupos
@login_required
@permission_required("auth.change_user", raise_exception=True)
def asignar_grupos(request, user_id):
    usuario = get_object_or_404(User, pk=user_id)

    if request.method == "POST":
        form = AsignarGruposForm(request.POST)
        if form.is_valid():
            # Clear existing groups and assign new ones
            usuario.groups.clear()
            usuario.groups.add(form.cleaned_data["grupo"])
            usuario.save()

            messages.success(
                request, f"Grupos asignados correctamente para {usuario.username}"
            )
            return redirect("lista_usuarios")
    else:
        # Pre-select the user and initialize the form
        form = AsignarGruposForm(initial={"usuarios": [usuario]})

    return render(
        request,
        "usuario/grupos/asignar_grupos.html",
        {"form": form, "usuario": usuario},
    )
