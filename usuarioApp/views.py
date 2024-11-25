# usuarioApp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserCreationFormWithGroup

def NuevoUsuario(request):
    if request.method == "POST":
        form = UserCreationFormWithGroup(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']  # Obtener el grupo seleccionado
            user.groups.add(group)  # Asignar el grupo al usuario
            user.save()
            messages.success(request, "Usuario creado con éxito!")
            return redirect('nuevo_usuario')  # Redirige para limpiar el formulario
    else:
        form = UserCreationFormWithGroup()

    return render(request, 'dashboard/nuevo_usuario.html', {'form': form})


