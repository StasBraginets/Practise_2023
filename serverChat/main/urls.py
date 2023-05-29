from django.urls import path
from . import views

urlpatterns = [
    path('', views.check, name='check'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]