from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Funciones Registro, Login

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password_auth"]:
            try:
                user = User.objects.create_user(username = request.POST["username"], email = request.POST["email"], password = request.POST["password"])
                user.save()
                return render(request, 'register.html', {"message_POST" : "Usuario registrado correctamente"})
            except:
                return render(request, 'register.html', {"message_POST" : "Usuario ya registrado o email mal introducido"})

        else:
            return render(request, 'register.html', {"message_POST" : "Las contraseñas no coinciden!"})
    return render(request, 'register.html')