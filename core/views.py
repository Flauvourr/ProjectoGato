from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as l
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Funciones Registro, Login

def menu(request):
    return render(request, 'menu.html')


def login(request):
    if request.method == "POST":
        user = authenticate(request, email = request.POST["email"], username = request.POST["username"], password = request.POST["password"])
        if not user:
            return render(request, 'login.html', {'message_POST' : "Compruebe que los datos solicitados coincidan"})
        else:
            l(request,user)
            return redirect('gatoapp')
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