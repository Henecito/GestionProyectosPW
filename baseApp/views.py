from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Vista para el dashboard principal
@login_required
def dashboard_view(request):
    return render(request, "dashboard/dashboard.html")


# Vista para el resumen del dashboard
@login_required
def resumen_view(request):
    return render(request, "dashboard/resumen.html")


# Vista para el login (procesa las credenciales)
def login_view(request):
    if request.user.is_authenticated:
        return redirect(
            "dashboard"
        )  # Si ya está autenticado, lo redirigimos al dashboard

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Intentamos autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si las credenciales son correctas, iniciamos sesión
            login(request, user)
            return redirect("dashboard")  # Redirigimos al dashboard
        else:
            # Si las credenciales son incorrectas, mostramos un mensaje de error
            error_message = "Usuario o contraseña incorrectos."
            return render(request, "login/login.html", {"error_message": error_message})

    return render(
        request, "login/login.html"
    )  # Si el método no es POST, simplemente renderizamos el formulario
