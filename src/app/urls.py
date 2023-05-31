from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('logar_usuario/', logar_usuario, name="logar_usuario"),
    path('deslogar_usuario/', deslogar_usuario, name="deslogar_usuario"),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
    path('cadastrar_usuario/', cadastrar_usuario, name="cadastrar_usuario"),
    path('', index, name="index"),

    path('infor/', infor, name="index"),
    path('pi', pi, name="index"),
    path('ob', ob, name="index"),
    path('ap', ap, name="index"),
    path('msg', msg, name="index"),
    path('inf', inf, name="index"),


    path('create_view/', create_view, name="create_view"),
    path('create_tipo/', create_tipo, name="create_tipo"),
    path('list_view/', list_view, name="list_view"),

    path('detail_view/<id>/', detail_view ),




    
    # path('', mysite, name='mysite'), 
]

