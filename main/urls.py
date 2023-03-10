from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.registerPage, name='register'),
    path('login', views.LoginPage)
]