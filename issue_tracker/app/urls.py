from turtle import title
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.loginPage, name='login'),
    path('login/', views.loginPage, name='login'),
    path('homepage/', views.homepage, name='homepage')
]