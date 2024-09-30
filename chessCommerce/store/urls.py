from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.login_user, name="logout"),
]
