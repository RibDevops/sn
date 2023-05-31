from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# from django import forms 


 
# relative import of forms
from app.models import *
from app.forms import *

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Numeracao.objects.all()
         
    return render(request, "sn/list_view.html", context)

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Numeracao.objects.get(id = id)
         
    return render(request, "sn/detail_view.html", context)



def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = NumeracaoForm(request.POST or None)
    if form.is_valid():
        form.save()

     # Selecionar campos específicos
    # fields_to_display = ['tipo_doc', 'numero_doc', 'description_doc']
    # form_fields = {field: form[field] for field in fields_to_display}
    # context['form_fields'] = form_fields
    
         
    context['form']= form
    return render(request, "sn/create_view.html", context)

def create_tipo(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = TipoForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "sn/create_tipo.html", context)




















@login_required(login_url='/logar_usuario')
def home(request):
    return render(request, 'home.html')

def deslogar_usuario(request):
    logout(request)
    return redirect('index')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'users/cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            # pegando código da empresa
            # user = User.objects.get(pk = request.user.id)
            # prof = user.get_profile()
            login(request, usuario)
            return redirect('home')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'users/login.html', {'form_login': form_login})


# def index(request):
#     return render(request, 'users/login.html')

@login_required(login_url='/logar_usuario')
def index(request):
    return render(request, 'users/login.html')

# @login_required(login_url='/logar_usuario')
# def deslogar_usuario(request):
#     logout(request)
#     return redirect('index')

@login_required(login_url='/logar_usuario')
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'users/alterar_senha.html', {'form_senha': form_senha})





def infor(request):
    return render(request, 'users/login.html')
def pi(request):
    return render(request, 'users/login.html')
def ob(request):
    return render(request, 'users/login.html')
def ap(request):
    return render(request, 'users/login.html')
def msg(request):
    return render(request, 'users/login.html')
def inf(request):
    return render(request, 'users/login.html')

