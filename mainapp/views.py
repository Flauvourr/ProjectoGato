from django.shortcuts import render
from .models import pregunta, respuesta
# Create your views here.

#///////////////////////////////////////////////////////////////////#
#                                                                   #
#   La app del Kahoot. Importa las preguntas y respuestas.          #
#                                                                   #
#///////////////////////////////////////////////////////////////////#

def mainapp(request):
    preguntas = pregunta.objects.all()
    respuestas = respuesta.objects.all()
    
    context = {
        'preguntas': preguntas,
        'respuestas': respuestas,
    }
    
    return render(request, "main.html", context)