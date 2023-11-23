import random
from django.shortcuts import render, HttpResponse
from .models import Pregunta, Respuesta
import django.contrib.messages as messages
from core.models import User_Data

#Variables Globales
numDePregunta = 1
resp_correctas = 0
nivel = 1

#Función que reinicia el juego
def clean_data(request):
    global numDePregunta, resp_correctas
    numDePregunta = 1; resp_correctas = 0; 
    for pregunta in Pregunta.objects.filter(pregunta_Usada = True):
        pregunta.pregunta_Usada = False
        pregunta.save()

#Función que carga la información del usuario
def load_user(request):
    global nivel
    nivel = User_Data.objects.filter(nombre = request.user).values_list("nivel")[0][0]

# Función main de la pagina gatoapp
def gatoapp(request):
    #variables
    global numDePregunta, resp_correctas, nivel
    resp_correctas_alert = resp_correctas
    nivel_completo = 0
    #Si se llega recien a la pagina o si recarga parte de 0 
    if request.method == "GET":
        clean_data(request)
        nivel_completo = -1
        if request.user.is_authenticated: #Si hay un usuario logueado carga su información
            load_user(request)
    #Para cambiar de nivel o repetirlo dependiendo de las buenas
    if numDePregunta == 6:
        if resp_correctas > 3:
            nivel+=1
            nivel_completo = 1
            try: #Guarda el nivel logrado en la información del usuario logueado
                user_playing = User_Data.objects.get(nombre = request.user)
                user_playing.nivel = nivel
                user_playing.save()
            except:
                pass
        else:
            nivel_completo = 0
        clean_data(request)
        
    #Si responde una alternativa y es correcta se suma una respuesta correcta
    if request.method == "POST":
        if Respuesta.objects.filter(id = request.POST["respuesta"]).values_list("respuesta_Correcto")[0][0] == True:
            resp_correctas += 1
    #Saca todas las preguntas que no hayan sido usadas antes.
    preguntasDisponibles = Pregunta.objects.filter(pregunta_Usada=False)
    
    #Sortea las preguntas.
    preguntasElegidas = random.sample(list(preguntasDisponibles), 1)
    
    for preguntaElegida in preguntasElegidas:
        preguntaElegida.pregunta_Usada = True 
        preguntaElegida.save()

    respuestasPorPregunta = {}
    for pregunta in preguntasElegidas:

        respuestasTexto = Respuesta.objects.filter(pregunta_Origen=pregunta)

        respuestasPorPregunta[pregunta] = respuestasTexto

    context = {
        'preguntasElegidas': preguntasElegidas,
        'respuestasPorPregunta': respuestasPorPregunta,
        'numDePregunta' : numDePregunta,
        'nivel' : nivel,
        'resp_correctas_alert' : resp_correctas_alert,
        'nivel_completo' : nivel_completo,
    }

    numDePregunta+=1
    return render(request, "gatoapp.html", context)