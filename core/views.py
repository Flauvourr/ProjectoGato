from django.shortcuts import render
from django.http import HttpResponse

# Funciones Registro, Login

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')