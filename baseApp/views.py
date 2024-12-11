from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from baseApp.forms import EstadoForm, GroupForm
from baseApp.models import Estado, CustomGroup, Permission

# Vista principal
@login_required
def inicio(request):
    return render(request, "index.html")


# Estado
def gestionar_estados(request, estado_id=None):
    # Si se proporciona un estado_id, estamos en modo edición
    estado = get_object_or_404(Estado, id=estado_id) if estado_id else None

    # Manejar la creación o edición de un estado
    if request.method == "POST":
        form = EstadoForm(request.POST, instance=estado)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Estado guardado exitosamente.")
                return redirect("gestionar_estados")
            except Exception as e:
                messages.error(request, f"Error al guardar el estado: {str(e)}")
    else:
        form = EstadoForm(instance=estado)

    # Obtener estados agrupados por modelo
    estados_por_modelo = {
        modelo: Estado.objects.filter(modelo=modelo)
        for modelo, _ in Estado.MODELOS_CHOICES
    }

    data = {
        "form": form,
        "estados_por_modelo": estados_por_modelo,
        "estado_editando": estado,
    }

    return render(request, "base/estado/list.html", data)


def editar_estado(request, estado_id):
    estado = get_object_or_404(Estado, id=estado_id)

    if request.method == "POST":
        form = EstadoForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()
            messages.success(request, "Estado actualizado exitosamente.")
            return redirect("gestionar_estados")
    else:
        form = EstadoForm(instance=estado)

    data = {"form": form, "estado": estado}

    return render(request, "base/estado/form.html", data)


def eliminar_estado(request, estado_id):
    estado = get_object_or_404(Estado, id=estado_id)

    try:
        estado.delete()
        messages.success(request, "Estado eliminado exitosamente.")
    except Exception as e:
        messages.error(request, f"No se puede eliminar el estado: {str(e)}")

    return redirect("gestionar_estados")


# Grupos y permisos
@login_required
@permission_required('auth.view_group', raise_exception=True)
def manage_groups(request):
    # Formulario para crear un nuevo grupo
    if request.method == 'POST' and 'create_group' in request.POST:
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request, f'Grupo {group.name} creado exitosamente')
            return redirect('manage_groups')
    else:
        form = GroupForm()

    # Obtener grupos y permisos
    groups = Group.objects.all()
    
    # Obtener permisos de aplicaciones específicas
    content_types = ContentType.objects.filter(
        app_label__in=['proyectoApp', 'usuarioApp']
    )
    permissions = Permission.objects.filter(content_type__in=content_types)

    # Formulario para gestionar permisos de grupos
    if request.method == 'POST' and 'update_permissions' in request.POST:
        group_id = request.POST.get('group')
        group = get_object_or_404(Group, id=group_id)
        
        # Limpiar permisos actuales
        group.permissions.clear()
        
        # Añadir permisos seleccionados
        selected_permissions = request.POST.getlist('permissions')
        for perm_id in selected_permissions:
            permission = Permission.objects.get(id=perm_id)
            group.permissions.add(permission)
        
        messages.success(request, f'Permisos del grupo {group.name} actualizados')
        return redirect('manage_groups')

    context = {
        'form': form,
        'groups': groups,
        'permissions': permissions,
    }
    return render(request, 'base/grupo/manage_groups.html', context)

@login_required
@permission_required('auth.delete_group', raise_exception=True)
def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group.delete()
    messages.success(request, f'Grupo {group.name} eliminado exitosamente')
    return redirect('manage_groups')