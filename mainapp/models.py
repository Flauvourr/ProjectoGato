from django.db import models

#///////////////////////////////////////////////////////////////////#
#                                                                   #
#   Modelo de las preguntas del Kahoot. Longitud máx de la pregunta #
#   es de 120 carácteres.                                           #
#                                                                   #
#///////////////////////////////////////////////////////////////////#
class pregunta(models.Model):
    enunciado = models.CharField(max_length=120)
    
    def __str__(self):
        return self.enunciado

#///////////////////////////////////////////////////////////////////#
#                                                                   #
#   Modelo de las respuestas del Kahoot. Largo máximo por respuesta #
#   es de 100 carácteres.                                           #
#                                                                   #
#   Cada respuesta está asociada a alguna pregunta con la           #
#   ForeignKey.                                                     #
#                                                                   #
#   Además, tiene un booleano asociado que indica si es la          #
#   respuesta correcta o no.                                        #
#                                                                   #
#///////////////////////////////////////////////////////////////////#
class respuesta(models.Model):
    resp = models.CharField(max_length=100)
    es_correcto = models.BooleanField(default=False)
    
    preg = models.ForeignKey(pregunta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.resp