from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Funciones Registro, Login

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password_auth"]:
            user = User.objects.create_user(username = request.POST["username"], email = request.POST["email"], password = request.POST["password"])
            user.save()
            return HttpResponse("Usuario creado correctamente")
        else:
            return HttpResponse("Las contraseñas no coinciden")
    return render(request, 'register.html')