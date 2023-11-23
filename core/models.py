from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class User_Data(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField()