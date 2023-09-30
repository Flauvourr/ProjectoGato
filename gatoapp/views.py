import random
from django.shortcuts import render, HttpResponse
from .models import Pregunta, Respuesta

# Create your views here.
def gatoapp(request):
    #Saca todas las preguntas que no hayan sido usadas antes.
    preguntasDisponibles = Pregunta.objects.filter(pregunta_Usada=False)
    print(preguntasDisponibles)
    #En caso de que no hayan preguntas, manda el warning.
    if preguntasDisponibles.count()==0:
        return HttpResponse('No hay nada añadido aún')
    
    #Si hay preguntas añadidas, sigue.
    preguntasElegidas = random.sample(list(preguntasDisponibles), 1)
    print(preguntasElegidas)
    
    # for preguntaElegida in preguntasElegidas:
    #     preguntaElegida.pregunta_Usada = True 
    #     preguntaElegida.save()

    respuestasPorPregunta = {}
    for pregunta in preguntasElegidas:
        print(pregunta)
        respuestasTexto = Respuesta.objects.filter(pregunta_Origen=pregunta)
        print(respuestasTexto)
        respuestasPorPregunta[pregunta] = respuestasTexto
        print(respuestasPorPregunta)
    context = {
        'preguntasElegidas': preguntasElegidas,
        'respuestasPorPregunta': respuestasPorPregunta,
    }
    
    return render(request, "gatoapp.html", context)