from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, View
from django.contrib.auth.views import PasswordChangeView

from .models import Area, SubArea, Empleado, Asignar
from .forms import AreaForm, SubAreaForm, EmpleadoForm, AsignarForm, PasswordChangeFormCustom, AsignarUsuariosAGrupoForm

from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Vista para Área
class AreaListView(LoginRequiredMixin, ListView):
    model = Area
    template_name = "usuario/area/area_list.html"
    context_object_name = "areas"


class AreaCreateView(LoginRequiredMixin, CreateView):
    model = Area
    form_class = AreaForm
    template_name = "usuario/area/area_form.html"
    success_url = reverse_lazy("area_list")

    def form_valid(self, form):
        messages.success(self.request, "Área creada exitosamente.")
        return super().form_valid(form)


class AreaUpdateView(LoginRequiredMixin, UpdateView):
    model = Area
    form_class = AreaForm
    template_name = "usuario/area/area_form.html"
    success_url = reverse_lazy("area_list")

    def form_valid(self, form):
        messages.success(self.request, "Área actualizada exitosamente.")
        return super().form_valid(form)


class AreaDeleteView(LoginRequiredMixin, DeleteView):
    model = Area
    template_name = "usuario/area/area_confirm_delete.html"
    success_url = reverse_lazy("area_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Área eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)


# Vista para SubÁrea
class SubAreaListView(LoginRequiredMixin, ListView):
    model = SubArea
    template_name = "usuario/area/subarea/subarea_list.html"
    context_object_name = "subareas"


class SubAreaCreateView(LoginRequiredMixin, CreateView):
    model = SubArea
    form_class = SubAreaForm
    template_name = "usuario/area/subarea/subarea_form.html"
    success_url = reverse_lazy("subarea_list")

    def form_valid(self, form):
        messages.success(self.request, "SubÁrea creada exitosamente.")
        return super().form_valid(form)


class SubAreaUpdateView(LoginRequiredMixin, UpdateView):
    model = SubArea
    form_class = SubAreaForm
    template_name = "usuario/area/subarea/subarea_form.html"
    success_url = reverse_lazy("subarea_list")

    def form_valid(self, form):
        messages.success(self.request, "SubÁrea actualizada exitosamente.")
        return super().form_valid(form)


class SubAreaDeleteView(LoginRequiredMixin, DeleteView):
    model = SubArea
    template_name = "usuario/area/subarea/subarea_confirm_delete.html"
    success_url = reverse_lazy("subarea_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "SubÁrea eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)


# Vista para Empleado
class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = "usuario/empleados/empleado_list.html"
    context_object_name = "empleados"


class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "usuario/empleados/empleado_form.html"
    success_url = reverse_lazy("empleado_list")

    def form_valid(self, form):
        messages.success(self.request, "Empleado creado exitosamente.")
        return super().form_valid(form)


class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "usuario/empleados/empleado_form.html"
    success_url = reverse_lazy("empleado_list")

    def form_valid(self, form):
        messages.success(self.request, "Empleado actualizado exitosamente.")
        return super().form_valid(form)


class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = "usuario/empleados/empleado_confirm_delete.html"
    success_url = reverse_lazy("empleado_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Empleado eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)


# Vista para Asignar
class AsignarListView(LoginRequiredMixin, ListView):
    model = Asignar
    template_name = "asignar_list.html"
    context_object_name = "asignaciones"


class AsignarCreateView(LoginRequiredMixin, CreateView):
    model = Asignar
    form_class = AsignarForm
    template_name = "asignar_form.html"
    success_url = reverse_lazy("asignar_list")

    def form_valid(self, form):
        messages.success(self.request, "Asignación creada exitosamente.")
        return super().form_valid(form)


class AsignarUpdateView(LoginRequiredMixin, UpdateView):
    model = Asignar
    form_class = AsignarForm
    template_name = "asignar_form.html"
    success_url = reverse_lazy("asignar_list")

    def form_valid(self, form):
        messages.success(self.request, "Asignación actualizada exitosamente.")
        return super().form_valid(form)


class AsignarDeleteView(LoginRequiredMixin, DeleteView):
    model = Asignar
    template_name = "asignar_confirm_delete.html"
    success_url = reverse_lazy("asignar_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Asignación eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "usuario/usuarios/lista_usuarios.html" 
    context_object_name = "usuarios"

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeFormCustom  # Tu formulario personalizado
    template_name = 'usuario/perfil/password_change_form.html'
    success_url = reverse_lazy("password_change")  # Redirigir a la página de inicio tras un cambio exitoso

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
    
#Grupos
class AsignarUsuariosAGrupoView(View):
    def get(self, request):
        form = AsignarUsuariosAGrupoForm()
        return render(request, 'usuario/grupos/asignar_grupo.html', {'form': form})

    def post(self, request):
        form = AsignarUsuariosAGrupoForm(request.POST)
        if form.is_valid():
            usuarios = form.cleaned_data['usuarios']
            grupo = form.cleaned_data['grupo']

            # Asignar los usuarios seleccionados al grupo
            for usuario in usuarios:
                usuario.groups.add(grupo)
                messages.success(request, f"Usuario {usuario.username} asignado a {grupo.name}.")

            return redirect('inicio')  # Redirige a la misma página o a otra

        return render(request, 'usuario/grupos/asignar_grupo.html', {'form': form})
    