from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from baseApp.forms import EstadoForm
from baseApp.models import Estado


# Vista principal
@login_required
def inicio(request):
    return render(request, "index.html")


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
