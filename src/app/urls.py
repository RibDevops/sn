from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('home', home, name='home'),
    path('logar_usuario', logar_usuario, name="logar_usuario"),
    path('deslogar_usuario', deslogar_usuario, name="deslogar_usuario"),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
    path('cadastrar_usuario', cadastrar_usuario, name="cadastrar_usuario"),
    path('', index, name="index"),
    
    # path('', mysite, name='mysite'), 
]

