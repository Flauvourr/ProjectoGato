from django.db import models

# Create your models here.

class pregunta(models.Model):
    enunciado = models.CharField(max_length=120)
    
    def __str__(self):
        return self.enunciado
    
class respuesta(models.Model):
    resp = models.CharField(max_length=100)
    es_correcto = models.BooleanField(default=False)
    
    preg = models.ForeignKey(pregunta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.resp