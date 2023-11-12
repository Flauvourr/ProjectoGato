import random
from django.shortcuts import render, HttpResponse
from .models import Pregunta, Respuesta

#Global variables
numDePregunta = 1
resp_correctas = 0
# Create your views here.
def gatoapp(request):
    global numDePregunta, resp_correctas
    #Si se llega recien a la pagina o si recarga parte de 0 
    if request.method == "GET":
        numDePregunta = 1; resp_correctas = 0
        for pregunta in Pregunta.objects.filter(pregunta_Usada = True):
            pregunta.pregunta_Usada = False
            pregunta.save()
    #Si responde una alternativa y es correcta se suma una respuesta correcta
    if request.method == "POST":
        if Respuesta.objects.filter(id = request.POST["respuesta"]).values_list("respuesta_Correcto")[0][0] == True:
            resp_correctas += 1
    #Saca todas las preguntas que no hayan sido usadas antes.
    preguntasDisponibles = Pregunta.objects.filter(pregunta_Usada=False)
    #En caso de que no hayan preguntas, manda el warning.
    if preguntasDisponibles.count()==0:
        return HttpResponse('No hay nada añadido aún')
    
    #Si hay preguntas añadidas, sigue.
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
    }
    print(resp_correctas)
    numDePregunta+=1
    return render(request, "gatoapp.html", context)