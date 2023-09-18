from django.contrib import admin
from .models import pregunta, respuesta

#///////////////////////////////////////////////////////////////////#
#                                                                   #
#   Hace que se puedan editar las preguntas y respuestas desde el   #
#   sitio de admin. Añadan /admin/ al final de la urly logueense.   #
#   Si no tienen cuenta, creen un superuser con el comando:         #
#   >>> python manage.py createsuperuser
#                                                                   #
#///////////////////////////////////////////////////////////////////#
admin.site.register(pregunta)
admin.site.register(respuesta)