from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission

from baseApp.forms import EstadoForm
from baseApp.models import Estado, CustomGroup, GroupPermission


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


# Grupo
@login_required
def manage_groups(request):
    if request.method == 'POST':
        # Crear nuevo grupo
        group_name = request.POST.get('new_group_name')
        if group_name:
            custom_group = CustomGroup.objects.create(
                name=group_name,
                base_group=Group.objects.create(name=group_name),
                owner=request.user
            )
            return redirect('manage_groups')
        
        # Actualizar permisos de grupos existentes
        for param, value in request.POST.items():
            if param.startswith('permission_'):
                permission_id = int(param.split('_')[1])
                group_id = int(param.split('_')[3])
                custom_group = get_object_or_404(CustomGroup, id=group_id)
                permission = Permission.objects.get(id=permission_id)
                
                if value == 'on':
                    custom_group.permissions.add(permission)
                    custom_group.base_group.permissions.add(permission)
                else:
                    custom_group.permissions.remove(permission)
                    custom_group.base_group.permissions.remove(permission)
        
    # Obtener todos los permisos y grupos del usuario
    permissions = Permission.objects.all()
    user_groups = CustomGroup.objects.filter(owner=request.user)
    
    context = {
        'permissions': permissions,
        'user_groups': user_groups
    }
    return render(request, 'base/grupo/manage_groups.html', context)