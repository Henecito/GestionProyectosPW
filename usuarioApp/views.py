from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def NuevoUsuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado con éxito!")
            return redirect('nuevo_usuario')  # Redirige para limpiar el formulario
    else:
        form = UserCreationForm()

    return render(request, 'dashboard/nuevo_usuario.html', {'form': form})


