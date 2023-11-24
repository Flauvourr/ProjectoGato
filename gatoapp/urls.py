from django.urls import path
from . import views

urlpatterns = [
    path("", views.gatoapp, name="gatoapp"),
    path("lobby", views.lobby, name="lobby")
]