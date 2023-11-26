from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.menu, name = "menu"),
    path("", views.home, name = "home"),
    path("login/", views.login, name="login"),
    path("login/register/", views.register, name="register")
]