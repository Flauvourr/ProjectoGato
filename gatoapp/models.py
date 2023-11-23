from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Pregunta(models.Model):
    pregunta_Texto = models.CharField(max_length=160)
    pregunta_Usada = models.BooleanField(default=False)

    def __str__(self):
        return self.pregunta_Texto
    
class Respuesta(models.Model):
    respuesta_Texto = models.CharField(max_length=100)
    respuesta_Correcto = models.BooleanField(default=False)

    pregunta_Origen = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return self.respuesta_Texto

